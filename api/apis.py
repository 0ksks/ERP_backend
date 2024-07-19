import base64
import importlib
import json
from dataclasses import dataclass, asdict
from typing import Any, TypeVar, Type, Literal

import stringcase
from flask import Blueprint, request
from sqlalchemy_serializer import SerializerMixin
from stringcase import snakecase

from model.repositories import BaseRepository

ResponseData = TypeVar('ResponseData', dict[str, Any], list[dict[str, Any]])


def dict2base64(data):
    json_str = json.dumps(data)
    base64_bytes = base64.b64encode(json_str.encode('utf-8'))
    return base64_bytes.decode('utf-8')


def base642dict(base64_str):
    try:
        json_bytes = base64.b64decode(base64_str)
        data = json.loads(json_bytes.decode('utf-8'))
        return data
    finally:
        return None


@dataclass
class Response:
    code: int
    message: str
    data: ResponseData

    @property
    def json(self) -> str:
        body = asdict(self)
        if body["data"] is None:
            body["data"] = {}
        return json.dumps(body)

    @staticmethod
    def create_success(data: ResponseData):
        return Response(code=201, message="success", data=data).json, 201

    @staticmethod
    def update_success():
        return Response(code=200, message="success", data={}).json, 200

    @staticmethod
    def not_found(entity: str):
        return Response(code=404, message=f"{stringcase.snakecase(entity).replace("_", " ")} not found",
                        data=[]).json, 200

    @staticmethod
    def query_success(data: ResponseData):
        return Response(code=200, message="success", data=data).json, 200


class Controller:
    def __init__(self, entityName: str, repository: Type[BaseRepository], blueprint: Blueprint, env: str):
        self.repository = repository
        self.blueprint = blueprint
        self.entityName = entityName
        self.entityIDKey = stringcase.camelcase(entityName) + "ID"
        self.register_routes(env)

    def register_routes(self, env: str):
        if env == "dev":
            self.blueprint.route('/create', methods=['POST'])(self.create)
            self.blueprint.route('/update', methods=['PATCH'])(self.update)
            self.blueprint.route('/query', methods=['GET'])(self.query)
        elif env == "test":
            self.blueprint.route('/create_success', methods=['POST'])(self.create)
            self.blueprint.route('/update_success', methods=['PATCH'])(self.update)
            self.blueprint.route('/update_not_found', methods=['PATCH'])(self.update)
            self.blueprint.route('/query_success', methods=['GET'])(self.query)
            self.blueprint.route('/query_not_found', methods=['GET'])(self.query)
        else:
            raise Exception(f"env {env} undefined")

    def create(self):
        data = request.json
        instance: SerializerMixin = self.repository.create(kwargs=data)
        entityIDValue = instance.to_dict()[self.entityIDKey]
        return Response.create_success({self.entityIDKey: entityIDValue})

    def update(self):
        data: dict = request.json
        ID = data.get(self.entityIDKey)
        if ID is None:
            authHeader = request.headers.get('Authorization')
            token = authHeader.split(" ")[1]
            decodedToken = base642dict(token)
            ID = decodedToken.get("userID")

        instance = self.repository.update(ID=ID, kwargs=data)
        if instance:
            return Response.update_success()
        else:
            return Response.not_found(self.entityName)

    def query(self):
        data = request.json
        ID = data.get(self.entityIDKey, None)
        if ID:
            instance = self.repository.get(ID=ID)
        else:
            instance = self.repository.query_list(kwargs=data)
        if instance:
            if not isinstance(instance, list):
                instance = [instance, ]
            return Response.query_success(list(map(lambda i: i.to_dict(), instance)))
        else:
            return Response.not_found(self.entityName)

    @classmethod
    def register_entity(cls, entityName: str, env: Literal["test", "dev"] = "test"):
        module = importlib.import_module("model.repositories")
        EntityRepository = getattr(module, f"{entityName}Repository")
        EntityBlueprint = Blueprint(entityName, __name__, url_prefix=f"/api/{snakecase(entityName)}")
        return cls(entityName, EntityRepository(), EntityBlueprint, env).blueprint


class UserController(Controller):
    def register_routes(self, env: str):
        if env == "dev":
            self.blueprint.route('/login', methods=['POST'])(self.login)
            self.blueprint.route('/register', methods=['POST'])(self.register)
            self.blueprint.route('/change_password', methods=['POST'])(self.change_password)
        elif env == "test":
            self.blueprint.route('/login_success', methods=['POST'])(self.login)
            self.blueprint.route('/login_not_found', methods=['POST'])(self.login)
            self.blueprint.route('/login_wrong_password', methods=['POST'])(self.login)
            self.blueprint.route('/register_success', methods=['POST'])(self.register)
            self.blueprint.route('/change_password_success', methods=['POST'])(self.change_password)
            self.blueprint.route('/change_password_wrong', methods=['POST'])(self.change_password)
        else:
            raise Exception(f"env {env} undefined")

    def login(self):
        data = request.json
        ID = data.get("userID")
        instance = self.repository.get(ID=ID)
        password = data.get("password")
        if instance:  # 用户存在
            if password == instance.password:  # 密码正确
                dataNoToken = {"userID": instance.userID, "role": instance.role}
                token = dict2base64(dataNoToken)
                dataToken = dataNoToken
                dataToken["token"] = token
                return Response(code=201, message="success",
                                data=dataToken).json, 201
            else:  # 密码错误
                return Response(code=401, message="wrong password", data={}).json, 200
        else:  # 用户不存在
            return Response.not_found(self.entityName)

    def register(self):
        data = request.json
        instance = self.repository.create(kwargs=data)
        userID = instance.userID
        return Response.create_success({"userID": userID})

    def change_password(self):
        data = request.json
        oldPasswordInput = data.get("oldPassword")
        oldPasswordReal = self.repository.get(ID=data.get("userID")).password
        print(oldPasswordInput, oldPasswordReal)
        if oldPasswordInput == oldPasswordReal:
            self.repository.update(ID=data.get("userID"), kwargs={"password": data.get("newPassword")})
            return Response.update_success()
        else:
            return Response(code=401, message="wrong password", data={}).json, 200

    @classmethod
    def register_entity(cls, entityName: str = "User", env: Literal["test", "dev"] = "test"):
        if entityName != "User":
            raise Warning(f"entity name {entityName} must be User")
        entityName = "User"
        return super().register_entity(entityName, env)


class DocumentFlowController(Controller):
    def register_routes(self, env: str):
        if env == "dev":
            self.blueprint.route('/display', methods=["GET"])(self.query)
        elif env == "test":
            self.blueprint.route('/display_success/finished', methods=["GET"])(self.query)
            self.blueprint.route('/display_success/unfinished', methods=["GET"])(self.query)
            self.blueprint.route('/display_not_found', methods=["GET"])(self.query)
