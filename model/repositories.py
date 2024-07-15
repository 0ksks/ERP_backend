from typing import TypeVar, Generic, Type, Optional, NewType, Any
from . import models, db
from flask_sqlalchemy.model import Model

T = TypeVar("T", bound=Model)
PrimaryKey = NewType("PrimaryKey", Any)


class BaseRepository(Generic[T]):
    model: Type[T] = None

    def get(
        self, id: PrimaryKey
    ) -> Optional[T]:  # 用于主键查询，返回一条数据，get方法不能使用键值对，只能接收单值
        return self.model.query.get(id)

    def query_list(
        self, kwargs: dict[str, Any]
    ) -> list[T]:  # 用于模糊条件查询，返回多条数据
        return self.model.query.filter_by(**kwargs).all()

    def query_one(
        self, kwargs: dict[str, Any]
    ) -> Optional[T]:  # 用于条件查询，此时返回一条数据
        return self.model.query.filter_by(**kwargs).first()

    def create(self, kwargs: dict[str, Any]) -> T:  # 创建新数据
        instance = self.model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance

    def update(
        self, id: PrimaryKey, kwargs: dict[str, Any]
    ) -> Optional[T]:  # 更新数据，id为对应表主键，kwargs为需要更新的内容
        instance = self.get(id)
        if instance is None:
            return None
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        db.session.commit()
        return instance


# 定义具体的Repository类并指定模型类型
class UserRepository(BaseRepository[models.User]):
    model = models.User


class SupplierRepository(BaseRepository[models.Supplier]):
    model = models.Supplier


class MaterialRepository(BaseRepository[models.Material]):
    model = models.Material


class StockRepository(BaseRepository[models.Stock]):
    model = models.Stock


class PurchaseOrderRepository(BaseRepository[models.PurchaseOrder]):
    model = models.PurchaseOrder


class GoodsReceiptRepository(BaseRepository[models.GoodsReceipt]):
    model = models.GoodsReceipt


class DocumentFlowRepository(BaseRepository[models.DocumentFlow]):
    model = models.DocumentFlow
