from typing import TypeVar, Generic, Type, Optional, NewType, Any

from flask_sqlalchemy.model import Model

from . import models, db

# 定义一个类型变量T，限制为Model的子类
T = TypeVar("T", bound=Model)

# 定义一个新的类型PrimaryKey，用于表示主键，可以是任何类型
PrimaryKey = NewType("PrimaryKey", Any)


# 基础仓库类，用于处理通用的数据库操作
class BaseRepository(Generic[T]):
    model: Type[T] = None  # 指定模型类型，默认为None

    # 根据主键ID查询数据，返回一个Optional类型的模型实例
    def get(
        self, ID: PrimaryKey
    ) -> Optional[T]:  # 用于主键查询，返回一条数据，get方法不能使用键值对，只能接收单值
        return self.model.query.get(ID)

    # 根据条件查询多条数据，返回模型实例的列表
    def query_list(
        self, kwargs: dict[str, Any]
    ) -> list[T]:  # 用于模糊条件查询，返回多条数据
        if len(kwargs) > 0:
            return self.model.query.filter_by(**kwargs).all()
        else:
            return self.model.query.all()

    # 根据条件查询一条数据，返回一个Optional类型的模型实例
    def query_one(
        self, kwargs: dict[str, Any]
    ) -> Optional[T]:  # 用于条件查询，此时返回一条数据
        return self.model.query.filter_by(**kwargs).first()

    # 创建新数据，接收一个包含数据的字典作为参数，返回创建的模型实例
    def create(self, kwargs: dict[str, Any]) -> T:  # 创建新数据
        instance = self.model(**kwargs)  # 使用关键字参数创建模型实例
        db.session.add(instance)  # 将实例添加到数据库会话
        db.session.commit()  # 提交事务保存数据
        return instance

    # 更新数据，接收主键ID和需要更新的数据字典作为参数，返回更新后的模型实例
    def update(
        self, ID: PrimaryKey, kwargs: dict[str, Any]
    ) -> Optional[T]:  # 更新数据，id为对应表主键，kwargs为需要更新的内容
        instance = self.get(ID)  # 根据ID获取实例
        if instance is None:  # 如果实例不存在，返回None
            return None
        for attr, value in kwargs.items():  # 遍历要更新的字段和值
            setattr(instance, attr, value)  # 设置实例的属性
        db.session.commit()  # 提交事务保存更新
        return instance


# 定义具体的Repository类，并指定模型类型


# 用户仓库类，处理User模型的数据操作
class UserRepository(BaseRepository[models.User]):
    model = models.User


# 供应商仓库类，处理Supplier模型的数据操作
class SupplierRepository(BaseRepository[models.Supplier]):
    model = models.Supplier


# 材料仓库类，处理Material模型的数据操作
class MaterialRepository(BaseRepository[models.Material]):
    model = models.Material


# 库存仓库类，处理Stock模型的数据操作
class StockRepository(BaseRepository[models.Stock]):
    model = models.Stock


# 采购订单仓库类，处理PurchaseOrder模型的数据操作
class PurchaseOrderRepository(BaseRepository[models.PurchaseOrder]):
    model = models.PurchaseOrder


# 收货单仓库类，处理GoodsReceipt模型的数据操作
class GoodsReceiptRepository(BaseRepository[models.GoodsReceipt]):
    model = models.GoodsReceipt


# 文档流仓库类，处理DocumentFlow模型的数据操作
class DocumentFlowRepository(BaseRepository[models.DocumentFlow]):
    model = models.DocumentFlow
