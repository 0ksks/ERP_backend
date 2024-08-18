import base64
import importlib
import json
from dataclasses import dataclass, asdict
from typing import Any, TypeVar, Type, Literal

import stringcase
from flask import Blueprint, request
from sqlalchemy_serializer import SerializerMixin

from model.repositories import BaseRepository, DocumentFlowRepository

# 定义一个泛型类型，表示响应数据，可以是字典或字典列表
ResponseData = TypeVar("ResponseData", dict[str, Any], list[dict[str, Any]])


# 将字典数据编码为base64字符串的函数
def dict2base64(data):
    json_str = json.dumps(data)  # 将字典转换为JSON字符串
    base64_bytes = base64.b64encode(
        json_str.encode("utf-8")
    )  # 将JSON字符串编码为base64
    return base64_bytes.decode("utf-8")  # 将base64字节转换为字符串并返回


# 将base64字符串解码为字典的函数
def base642dict(base64_str):
    try:
        json_bytes = base64.b64decode(base64_str)  # 将base64字符串解码为字节
        data = json.loads(
            json_bytes.decode("utf-8")
        )  # 将字节转换为JSON字符串再转为字典
        return data
    finally:
        return None  # 确保在出现错误时返回None


# 使用dataclass定义一个标准化的API响应类
@dataclass
class Response:
    code: int  # HTTP状态码
    message: str  # 响应消息
    data: ResponseData  # 数据负载

    # 将响应转换为JSON格式的属性
    @property
    def json(self) -> str:
        body = asdict(self)  # 将dataclass实例转换为字典
        if body["data"] is None:
            body["data"] = {}  # 如果'data'为None，设置为一个空字典
        return json.dumps(body)  # 将字典转换为JSON字符串

    # 创建成功响应的静态方法，适用于创建操作
    @staticmethod
    def create_success(data: ResponseData):
        return Response(code=201, message="success", data=data).json, 201

    # 创建成功响应的静态方法，适用于更新操作
    @staticmethod
    def update_success():
        return Response(code=200, message="success", data={}).json, 200

    # 创建找不到资源的响应的静态方法
    @staticmethod
    def not_found(entity: str):
        return (
            Response(
                code=404,
                message=f"{stringcase.snakecase(entity).replace('_', ' ' )} not found",
                data=[],
            ).json,
            200,
        )

    # 创建查询成功响应的静态方法
    @staticmethod
    def query_success(data: ResponseData):
        return Response(code=200, message="success", data=data).json, 200


# 基础控制器类，处理基本的CRUD操作
class Controller:
    def __init__(
        self,
        entityName: str,  # 实体名称
        repository: Type[BaseRepository],  # 仓库类，用于数据库操作
        blueprint: Blueprint,  # Flask Blueprint，用于路由
        env: str,  # 运行环境
    ):
        self.repository = repository  # 数据库操作的仓库
        self.blueprint = blueprint  # Flask的Blueprint，用于注册路由
        self.entityName = entityName  # 当前控制器处理的实体名称
        self.entityIDKey = (
            stringcase.camelcase(entityName) + "ID"
        )  # 实体ID字段，使用驼峰命名法
        self.register_routes(env)  # 根据环境注册路由

    # 根据运行环境注册路由的方法（开发环境或测试环境）
    def register_routes(self, env: str):
        if env == "dev":
            self.blueprint.route("/create", methods=["POST"])(self.create)
            self.blueprint.route("/update", methods=["PATCH"])(self.update)
            self.blueprint.route("/query", methods=["POST"])(self.query)
        elif env == "test":
            self.blueprint.route("/create_success", methods=["POST"])(self.create)
            self.blueprint.route("/update_success", methods=["PATCH"])(self.update)
            self.blueprint.route("/update_not_found", methods=["PATCH"])(self.update)
            self.blueprint.route("/query_success", methods=["GET"])(self.query)
            self.blueprint.route("/query_not_found", methods=["GET"])(self.query)
        else:
            raise Exception(f"env {env} undefined")

    # 处理实体创建的函数
    def create(self):
        data = request.json  # 从请求中获取JSON数据
        instance: SerializerMixin = self.repository.create(
            kwargs=data
        )  # 使用仓库创建实体实例
        entityIDValue = instance.to_dict()[self.entityIDKey]  # 从创建的实例中获取实体ID
        return Response.create_success(
            {self.entityIDKey: entityIDValue}
        )  # 返回成功响应

    # 处理实体更新的函数
    def update(self):
        data: dict = request.json  # 从请求中获取JSON数据
        ID = data.get(self.entityIDKey)  # 从请求数据中获取实体ID
        if ID is None:  # 如果请求数据中没有ID，从授权头中获取
            authHeader = request.headers.get("Authorization")
            token = authHeader.split(" ")[1]
            decodedToken = base642dict(token)
            ID = decodedToken.get("userID")

        instance = self.repository.update(ID=ID, kwargs=data)  # 在仓库中更新实体
        if instance:
            return Response.update_success()  # 如果更新成功，返回成功响应
        else:
            return Response.not_found(self.entityName)  # 如果未找到实体，返回404响应

    # 处理实体查询的函数
    def query(self):
        data = request.json  # 从请求中获取JSON数据
        ID = data.get(self.entityIDKey, None)  # 获取请求数据中的实体ID（如果有）
        if ID:
            instance = self.repository.get(ID=ID)  # 根据ID获取实体实例
        else:
            instance = self.repository.query_list(
                kwargs=data
            )  # 根据请求数据查询实体列表
        if instance:
            if not isinstance(instance, list):
                instance = [
                    instance,
                ]  # 确保返回的实例是一个列表
            return Response.query_success(
                list(map(lambda i: i.to_dict(), instance))
            )  # 返回查询成功的响应
        else:
            return Response.not_found(self.entityName)  # 如果未找到实体，返回404响应

    # 类方法，用于为给定的环境注册实体控制器
    @classmethod
    def register_entity(cls, entityName: str, env: Literal["test", "dev"] = "test"):
        module = importlib.import_module("model.repositories")  # 动态导入仓库模块
        EntityRepository = getattr(
            module, f"{entityName}Repository"
        )  # 获取实体对应的仓库类
        if env == "test":
            prefix = "/api/"
        else:
            prefix = "/"
        EntityBlueprint = Blueprint(
            entityName,
            __name__,
            url_prefix=f"{prefix}{stringcase.snakecase(entityName)}",
        )  # 为实体创建一个新的Flask Blueprint
        return cls(
            entityName, EntityRepository(), EntityBlueprint, env
        ).blueprint  # 返回注册后的Blueprint


# 专门处理用户相关操作的控制器类
class UserController(Controller):
    def register_routes(self, env: str):
        if env == "dev":
            self.blueprint.route("/login", methods=["POST"])(self.login)
            self.blueprint.route("/register", methods=["POST"])(self.register)
            self.blueprint.route("/change_password", methods=["POST"])(
                self.change_password
            )
        elif env == "test":
            self.blueprint.route("/login_success", methods=["POST"])(self.login)
            self.blueprint.route("/login_not_found", methods=["POST"])(self.login)
            self.blueprint.route("/login_wrong_password", methods=["POST"])(self.login)
            self.blueprint.route("/register_success", methods=["POST"])(self.register)
            self.blueprint.route("/change_password_success", methods=["POST"])(
                self.change_password
            )
            self.blueprint.route("/change_password_wrong", methods=["POST"])(
                self.change_password
            )
        else:
            raise Exception(f"env {env} undefined")

    # 处理用户登录的函数
    def login(self):
        data = request.json  # 从请求中获取JSON数据
        ID = data.get("userID")  # 从请求数据中获取用户ID
        instance = self.repository.get(ID=ID)  # 从仓库中获取用户实例
        password = data.get("password")  # 从请求数据中获取密码
        if instance:  # 如果用户存在
            if password == instance.password:  # 检查密码是否匹配
                dataNoToken = {"userID": instance.userID, "role": instance.role}
                token = dict2base64(dataNoToken)  # 将用户数据编码为base64 token
                dataToken = dataNoToken
                dataToken["token"] = token  # 在响应数据中添加token
                return Response(code=201, message="success", data=dataToken).json, 201
            else:  # 密码错误
                return Response(code=401, message="wrong password", data={}).json, 200
        else:  # 用户不存在
            return Response.not_found(self.entityName)

    # 处理用户注册的函数
    def register(self):
        data = request.json  # 从请求中获取JSON数据
        instance = self.repository.create(kwargs=data)  # 在仓库中创建新用户实例
        userID = instance.userID  # 从创建的实例中获取用户ID
        return Response.create_success({"userID": userID})  # 返回成功响应

    # 处理修改密码的函数
    def change_password(self):
        data = request.json  # 从请求中获取JSON数据
        oldPasswordInput = data.get("oldPassword")  # 获取请求中的旧密码
        oldPasswordReal = self.repository.get(
            ID=data.get("userID")
        ).password  # 从仓库中获取当前密码
        if oldPasswordInput == oldPasswordReal:
            self.repository.update(
                ID=data.get("userID"), kwargs={"password": data.get("newPassword")}
            )  # 在仓库中更新密码
            return Response.update_success()  # 返回成功响应
        else:
            return (
                Response(code=401, message="wrong password", data={}).json,
                200,
            )  # 如果密码不匹配，返回错误响应

    # 类方法，用于注册User实体控制器
    @classmethod
    def register_entity(
        cls, entityName: str = "User", env: Literal["test", "dev"] = "test"
    ):
        if entityName != "User":
            raise Warning(
                f"entity name {entityName} must be User"
            )  # 确保实体名称为'User'
        entityName = "User"
        return super().register_entity(entityName, env)


# 专门处理DocumentFlow相关操作的控制器类
class DocumentFlowController(Controller):
    def register_routes(self, env: str):
        if env == "dev":
            self.blueprint.route("/display", methods=["POST"])(self.query)
        elif env == "test":
            self.blueprint.route("/display_success/finished", methods=["GET"])(
                self.query
            )
            self.blueprint.route("/display_success/unfinished", methods=["GET"])(
                self.query
            )
            self.blueprint.route("/display_not_found", methods=["GET"])(self.query)


# 专门处理PurchaseOrder相关操作的控制器类
class PurchaseOrderController(Controller):
    # 重写create方法，以包含DocumentFlow的创建逻辑
    def create(self):
        response, _ = super().create()  # 调用基类的create方法
        responseData = json.loads(response)["data"]  # 获取创建的实体数据
        purchaseOrderID = responseData["purchaseOrderID"]  # 获取采购订单ID
        requestData = request.json  # 获取请求数据
        userID = requestData["userID"]  # 获取用户ID
        documentFlowRepository = DocumentFlowRepository()  # 创建DocumentFlow仓库实例
        instance: SerializerMixin = documentFlowRepository.create(
            dict(userID=userID, purchaseOrderID=purchaseOrderID)
        )  # 创建新的DocumentFlow实例
        entityIDValue = instance.to_dict()[self.entityIDKey]  # 获取创建的实体ID
        return Response.create_success(
            {self.entityIDKey: entityIDValue}
        )  # 返回成功响应


# 专门处理GoodsReceipt相关操作的控制器类
class GoodsReceiptController(Controller):
    # 重写create方法，将其与DocumentFlow关联
    def create(self):
        requestData = request.json  # 获取请求数据

        userID = requestData["userID"]
        purchaseOrderID = requestData["purchaseOrderID"]

        documentFlowRepository = DocumentFlowRepository()  # 创建DocumentFlow仓库实例
        documentFlowInstance: SerializerMixin = documentFlowRepository.query_one(
            dict(userID=userID, purchaseOrderID=purchaseOrderID)
        )  # 查询对应的DocumentFlow实例

        if documentFlowInstance:  # 如果找到DocumentFlow实例
            response, _ = super().create()  # 调用基类的create方法创建GoodsReceipt
            responseData = json.loads(response)["data"]  # 获取创建的GoodsReceipt数据
            goodsReceiptID = responseData[self.entityIDKey]  # 获取GoodsReceipt ID
            documentFlowID = documentFlowInstance.to_dict()[
                "documentID"
            ]  # 获取DocumentFlow ID
            documentFlowRepository.update(
                documentFlowID, dict(goodsReceiptID=goodsReceiptID)
            )  # 更新DocumentFlow，添加GoodsReceipt ID
            goodsReceiptInstance: SerializerMixin = self.repository.create(
                kwargs=requestData
            )  # 在仓库中创建GoodsReceipt
            entityIDValue = goodsReceiptInstance.to_dict()[
                self.entityIDKey
            ]  # 获取GoodsReceipt ID
            return Response.create_success(
                {self.entityIDKey: entityIDValue}
            )  # 返回成功响应
