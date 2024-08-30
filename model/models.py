from sqlalchemy import ForeignKey
from sqlalchemy_serializer import SerializerMixin

from . import db


# 数据库表对应ORM模型
class User(db.Model, SerializerMixin):
    __tablename__ = "User"
    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 从1开始
    username = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=True)


class Supplier(db.Model, SerializerMixin):
    __tablename__ = "Supplier"
    supplierID = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # 10000开始自增
    userID = db.Column(db.Integer, ForeignKey("User.userID"))
    supplierName = db.Column(db.String(255))
    address = db.Column(db.Text)
    communicationLang = db.Column(db.String(255))
    taxNumber = db.Column(db.Integer)
    companyCode = db.Column(db.String(255))
    reconciliationAcct = db.Column(db.String(255))
    termsOfPayment = db.Column(db.String(255))
    checkDoubleInvoice = db.Column(db.String(255))
    clerkName = db.Column(db.String(255))
    purchasingOrg = db.Column(db.String(255))
    orderCurrency = db.Column(db.String(255))
    partnerFunctions = db.Column(db.String(255))
    streetAddress = db.Column(db.String(255))
    postalCode = db.Column(db.String(255))
    country = db.Column(db.String(255))
    region = db.Column(db.String(255))
    city = db.Column(db.String(255))
    contactInfo = db.Column(db.String(255))
    discountConditions = db.Column(db.String(255))


class Material(db.Model, SerializerMixin):
    __tablename__ = "Material"
    materialID = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # 20000000开始自增
    userID = db.Column(db.Integer, ForeignKey("User.userID"))
    materialName = db.Column(db.String(255))
    description = db.Column(db.Text)
    baseUnit = db.Column(db.String(255))
    materialGroup = db.Column(db.String(255))
    division = db.Column(db.String(255))
    grossWeight = db.Column(db.Float)
    netWeight = db.Column(db.Float)
    weightUnit = db.Column(db.String(255))
    volume = db.Column(db.Float)
    volumeUnit = db.Column(db.String(255))
    packMaterial = db.Column(db.String(255))
    availabilityCheck = db.Column(db.String(255))
    transportationGroup = db.Column(db.String(255))
    loadingGroup = db.Column(db.String(255))
    mrpType = db.Column(db.String(255))
    mrpController = db.Column(db.String(255))
    lotSize = db.Column(db.String(255))
    minimumLotSize = db.Column(db.Integer)
    plannedDeliveryTime = db.Column(db.Date)
    valuationClass = db.Column(db.String(255))
    movingPrice = db.Column(db.Float)
    priceUnit = db.Column(db.String(255))
    standardPrice = db.Column(db.Float)


class Stock(db.Model, SerializerMixin):
    __tablename__ = "Stock"
    stockID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 从1开始自增
    userID = db.Column(db.Integer, ForeignKey("User.userID"))
    materialID = db.Column(db.Integer, db.ForeignKey("Material.materialID"))
    plant = db.Column(db.String(255))
    storageLocation = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    unitOfMeasure = db.Column(db.String(255))
    stockType = db.Column(db.String(255))
    valuationType = db.Column(db.String(255))
    batch = db.Column(db.String(255))
    specialStockIndicator = db.Column(db.String(255))
    companyCode = db.Column(db.String(255), default="US00")


class PurchaseOrder(db.Model, SerializerMixin):
    __tablename__ = "PurchaseOrder"
    purchaseOrderID = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # 40000000开始自增
    userID = db.Column(db.Integer, ForeignKey("User.userID"))
    supplierID = db.Column(db.Integer, db.ForeignKey("Supplier.supplierID"))
    stockID = db.Column(db.Integer, db.ForeignKey("Stock.stockID"))
    orderDate = db.Column(db.Date)
    deliveryDate = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    netPrice = db.Column(db.Float)
    currency = db.Column(db.String(255))
    purchasingGroup = db.Column(db.String(255))
    purchasingOrganization = db.Column(db.String(255))
    plant = db.Column(db.String(255))
    paymentTerms = db.Column(db.String(255))


class GoodsReceipt(db.Model, SerializerMixin):
    __tablename__ = "GoodsReceipt"
    goodsReceiptID = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # 从50000000自增
    userID = db.Column(db.Integer, ForeignKey("User.userID"))
    purchaseOrderID = db.Column(
        db.Integer, db.ForeignKey("PurchaseOrder.purchaseOrderID")
    )
    materialID = db.Column(db.Integer, db.ForeignKey("Material.materialID"))
    supplierID = db.Column(db.Integer, db.ForeignKey("Supplier.supplierID"))
    receiptDate = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    stockLocation = db.Column(db.String(255))
    batch = db.Column(db.String(255))
    plant = db.Column(db.String(255))
    movementType = db.Column(db.String(255))
    documentDate = db.Column(db.Date)
    postingDate = db.Column(db.Date)


class DocumentFlow(db.Model, SerializerMixin):
    __tablename__ = "DocumentFlow"
    documentID = db.Column(
        db.Integer, primary_key=True, autoincrement=True
    )  # 从60000000自增
    userID = db.Column(db.Integer, ForeignKey("User.userID"))
    purchaseOrderID = db.Column(db.Integer)
    goodsReceiptID = db.Column(db.Integer)
