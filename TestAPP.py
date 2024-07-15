import unittest
from app import app


"""
python -m unittest TestAPP.TestSupplier
"""
class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestSupplier.test_create_success
    """
    def test_create_success(self):
        
        response = self.app.post(
            "/api/supplier/create_success",
            json={"suppliername": "suppliername_value", "communicationLang": "communicationLang_value", "taxNumber": "taxNumber_value", "companyCode": "companyCode_value", "reconciliationAcct": "reconciliationAcct_value", "termsOfPayment": "termsOfPayment_value", "checkDoubleInvoice": "checkDoubleInvoice_value", "clerkName": "clerkName_value", "purchasingOrg": "purchasingOrg_value", "orderCurrency": "orderCurrency_value", "partnerFunctions": "partnerFunctions_value", "streetAddress": "streetAddress_value", "postalCode": "postalCode_value", "city": "city_value", "country": "country_value", "region": "region_value", "contactInfo": "contactInfo_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
    "code": 201,
    "message": "success",
    "data": {
        "supplierID": "supplierID_value"
    }
})


    """
    python -m unittest TestAPP.TestSupplier.test_update_success
    """
    def test_update_success(self):
        
        response = self.app.patch(
            "/api/supplier/update_success",
            json={"supplierID": "supplierID_value", "suppliername": "suppliername_value", "communicationLang": "communicationLang_value", "taxNumber": "taxNumber_value", "companyCode": "companyCode_value", "reconciliationAcct": "reconciliationAcct_value", "termsOfPayment": "termsOfPayment_value", "checkDoubleInvoice": "checkDoubleInvoice_value", "clerkName": "clerkName_value", "purchasingOrg": "purchasingOrg_value", "orderCurrency": "orderCurrency_value", "partnerFunctions": "partnerFunctions_value", "streetAddress": "streetAddress_value", "postalCode": "postalCode_value", "city": "city_value", "country": "country_value", "region": "region_value", "contactInfo": "contactInfo_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {}
})



    """
    python -m unittest TestAPP.TestSupplier.test_update_not_found
    """
    def test_update_not_found(self):
        
        response = self.app.patch(
            "/api/supplier/update_not_found",
            json={"supplierID": "supplierID_value", "suppliername": "suppliername_value", "communicationLang": "communicationLang_value", "taxNumber": "taxNumber_value", "companyCode": "companyCode_value", "reconciliationAcct": "reconciliationAcct_value", "termsOfPayment": "termsOfPayment_value", "checkDoubleInvoice": "checkDoubleInvoice_value", "clerkName": "clerkName_value", "purchasingOrg": "purchasingOrg_value", "orderCurrency": "orderCurrency_value", "partnerFunctions": "partnerFunctions_value", "streetAddress": "streetAddress_value", "postalCode": "postalCode_value", "city": "city_value", "country": "country_value", "region": "region_value", "contactInfo": "contactInfo_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "supplier not found",
    "data": []
})


    """
    python -m unittest TestAPP.TestSupplier.test_query_success
    """
    def test_query_success(self):
        
        response = self.app.get(
            "/api/supplier/query_success",
            json={"supplierID": "supplierID_value", "suppliername": "suppliername_value", "communicationLang": "communicationLang_value", "taxNumber": "taxNumber_value", "companyCode": "companyCode_value", "reconciliationAcct": "reconciliationAcct_value", "termsOfPayment": "termsOfPayment_value", "checkDoubleInvoice": "checkDoubleInvoice_value", "clerkName": "clerkName_value", "purchasingOrg": "purchasingOrg_value", "orderCurrency": "orderCurrency_value", "partnerFunctions": "partnerFunctions_value", "streetAddress": "streetAddress_value", "postalCode": "postalCode_value", "city": "city_value", "country": "country_value", "region": "region_value", "contactInfo": "contactInfo_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "supplierID": "supplierID_value1",
            "suppliername": "suppliername_value1",
            "communicationLang": "communicationLang_value1",
            "taxNumber": "taxNumber_value1",
            "companyCode": "companyCode_value1",
            "reconciliationAcct": "reconciliationAcct_value1",
            "termsOfPayment": "termsOfPayment_value1",
            "checkDoubleInvoice": "checkDoubleInvoice_value1",
            "clerkName": "clerkName_value1",
            "purchasingOrg": "purchasingOrg_value1",
            "orderCurrency": "orderCurrency_value1",
            "partnerFunctions": "partnerFunctions_value1",
            "streetAddress": "streetAddress_value1",
            "postalCode": "postalCode_value1",
            "city": "city_value1",
            "country": "country_value1",
            "region": "region_value1",
            "contactInfo": "contactInfo_value1",
            "userID": "userID_value1"
        },
        {
            "supplierID": "supplierID_value2",
            "suppliername": "suppliername_value2",
            "communicationLang": "communicationLang_value2",
            "taxNumber": "taxNumber_value2",
            "companyCode": "companyCode_value2",
            "reconciliationAcct": "reconciliationAcct_value2",
            "termsOfPayment": "termsOfPayment_value2",
            "checkDoubleInvoice": "checkDoubleInvoice_value2",
            "clerkName": "clerkName_value2",
            "purchasingOrg": "purchasingOrg_value2",
            "orderCurrency": "orderCurrency_value2",
            "partnerFunctions": "partnerFunctions_value2",
            "streetAddress": "streetAddress_value2",
            "postalCode": "postalCode_value2",
            "city": "city_value2",
            "country": "country_value2",
            "region": "region_value2",
            "contactInfo": "contactInfo_value2",
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestSupplier.test_query_not_found
    """
    def test_query_not_found(self):
        
        response = self.app.get(
            "/api/supplier/query_not_found",
            json={"supplierID": "supplierID_value", "suppliername": "suppliername_value", "communicationLang": "communicationLang_value", "taxNumber": "taxNumber_value", "companyCode": "companyCode_value", "reconciliationAcct": "reconciliationAcct_value", "termsOfPayment": "termsOfPayment_value", "checkDoubleInvoice": "checkDoubleInvoice_value", "clerkName": "clerkName_value", "purchasingOrg": "purchasingOrg_value", "orderCurrency": "orderCurrency_value", "partnerFunctions": "partnerFunctions_value", "streetAddress": "streetAddress_value", "postalCode": "postalCode_value", "city": "city_value", "country": "country_value", "region": "region_value", "contactInfo": "contactInfo_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "supplier not found",
    "data": []
})


"""
python -m unittest TestAPP.TestMaterial
"""
class TestMaterial(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestMaterial.test_create_success
    """
    def test_create_success(self):
        
        response = self.app.post(
            "/api/material/create_success",
            json={"materialName": "materialName_value", "description": "description_value", "baseUnit": "baseUnit_value", "materialGroup": "materialGroup_value", "division": "division_value", "grossWeight": 1.1, "netWeight": 1.1, "weightUnit": "weightUnit_value", "volume": 1.1, "volumeUnit": "volumeUnit_value", "packMaterial": "packMaterial_value", "availabilityCheck": "availabilityCheck_value", "transportationGroup": "transportationGroup_value", "loadingGroup": "loadingGroup_value", "mrpType": "mrpType_value", "mrpController": "mrpController_value", "lotSize": "lotSize_value", "minimumLotSize": 1, "plannedDeliveryTime": 1, "valuationClass": "valuationClass_value", "movingPrice": 1.1, "priceUnit": 1, "standardPrice": 1.1, "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
    "code": 201,
    "message": "success",
    "data": {
        "materialID": "materialID_value"
    }
})


    """
    python -m unittest TestAPP.TestMaterial.test_update_success
    """
    def test_update_success(self):
        
        response = self.app.patch(
            "/api/material/update_success",
            json={"materialID": "materialID_value", "materialName": "materialName_value", "description": "description_value", "baseUnit": "baseUnit_value", "materialGroup": "materialGroup_value", "division": "division_value", "grossWeight": 1.1, "netWeight": 1.1, "weightUnit": "weightUnit_value", "volume": 1.1, "volumeUnit": "volumeUnit_value", "packMaterial": "packMaterial_value", "availabilityCheck": "availabilityCheck_value", "transportationGroup": "transportationGroup_value", "loadingGroup": "loadingGroup_value", "mrpType": "mrpType_value", "mrpController": "mrpController_value", "lotSize": "lotSize_value", "minimumLotSize": 1, "plannedDeliveryTime": 1, "valuationClass": "valuationClass_value", "movingPrice": 1.1, "priceUnit": 1, "standardPrice": 1.1, "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {}
})



    """
    python -m unittest TestAPP.TestMaterial.test_update_not_found
    """
    def test_update_not_found(self):
        
        response = self.app.patch(
            "/api/material/update_not_found",
            json={"materialID": "materialID_value", "materialName": "materialName_value", "description": "description_value", "baseUnit": "baseUnit_value", "materialGroup": "materialGroup_value", "division": "division_value", "grossWeight": 1.1, "netWeight": 1.1, "weightUnit": "weightUnit_value", "volume": 1.1, "volumeUnit": "volumeUnit_value", "packMaterial": "packMaterial_value", "availabilityCheck": "availabilityCheck_value", "transportationGroup": "transportationGroup_value", "loadingGroup": "loadingGroup_value", "mrpType": "mrpType_value", "mrpController": "mrpController_value", "lotSize": "lotSize_value", "minimumLotSize": 1, "plannedDeliveryTime": 1, "valuationClass": "valuationClass_value", "movingPrice": 1.1, "priceUnit": 1, "standardPrice": 1.1, "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "material not found",
    "data": []
})


    """
    python -m unittest TestAPP.TestMaterial.test_query_success
    """
    def test_query_success(self):
        
        response = self.app.get(
            "/api/material/query_success",
            json={"materialID": "materialID_value", "materialName": "materialName_value", "description": "description_value", "baseUnit": "baseUnit_value", "materialGroup": "materialGroup_value", "division": "division_value", "grossWeight": 1.1, "netWeight": 1.1, "weightUnit": "weightUnit_value", "volume": 1.1, "volumeUnit": "volumeUnit_value", "packMaterial": "packMaterial_value", "availabilityCheck": "availabilityCheck_value", "transportationGroup": "transportationGroup_value", "loadingGroup": "loadingGroup_value", "mrpType": "mrpType_value", "mrpController": "mrpController_value", "lotSize": "lotSize_value", "minimumLotSize": 1, "plannedDeliveryTime": 1, "valuationClass": "valuationClass_value", "movingPrice": 1.1, "priceUnit": 1, "standardPrice": 1.1, "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "materialID": "materialID_value1",
            "materialName": "materialName_value1",
            "description": "description_value1",
            "baseUnit": "baseUnit_value1",
            "materialGroup": "materialGroup_value1",
            "division": "division_value1",
            "grossWeight": 1.1,
            "netWeight": 1.1,
            "weightUnit": "weightUnit_value1",
            "volume": 1.1,
            "volumeUnit": "volumeUnit_value1",
            "packMaterial": "packMaterial_value1",
            "availabilityCheck": "availabilityCheck_value1",
            "transportationGroup": "transportationGroup_value1",
            "loadingGroup": "loadingGroup_value1",
            "mrpType": "mrpType_value1",
            "mrpController": "mrpController_value1",
            "lotSize": "lotSize_value1",
            "minimumLotSize": 1,
            "plannedDeliveryTime": 1,
            "valuationClass": "valuationClass_value1",
            "movingPrice": 1.1,
            "priceUnit": 1,
            "standardPrice": 1.1,
            "userID": "userID_value1"
        },
        {
            "materialID": "materialID_value2",
            "materialName": "materialName_value2",
            "description": "description_value2",
            "baseUnit": "baseUnit_value2",
            "materialGroup": "materialGroup_value2",
            "division": "division_value2",
            "grossWeight": 2.2,
            "netWeight": 2.2,
            "weightUnit": "weightUnit_value2",
            "volume": 2.2,
            "volumeUnit": "volumeUnit_value2",
            "packMaterial": "packMaterial_value2",
            "availabilityCheck": "availabilityCheck_value2",
            "transportationGroup": "transportationGroup_value2",
            "loadingGroup": "loadingGroup_value2",
            "mrpType": "mrpType_value2",
            "mrpController": "mrpController_value2",
            "lotSize": "lotSize_value2",
            "minimumLotSize": 2,
            "plannedDeliveryTime": 2,
            "valuationClass": "valuationClass_value2",
            "movingPrice": 2.2,
            "priceUnit": 2,
            "standardPrice": 2.2,
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestMaterial.test_query_not_found
    """
    def test_query_not_found(self):
        
        response = self.app.get(
            "/api/material/query_not_found",
            json={"materialID": "materialID_value", "materialName": "materialName_value", "description": "description_value", "baseUnit": "baseUnit_value", "materialGroup": "materialGroup_value", "division": "division_value", "grossWeight": 1.1, "netWeight": 1.1, "weightUnit": "weightUnit_value", "volume": 1.1, "volumeUnit": "volumeUnit_value", "packMaterial": "packMaterial_value", "availabilityCheck": "availabilityCheck_value", "transportationGroup": "transportationGroup_value", "loadingGroup": "loadingGroup_value", "mrpType": "mrpType_value", "mrpController": "mrpController_value", "lotSize": "lotSize_value", "minimumLotSize": 1, "plannedDeliveryTime": 1, "valuationClass": "valuationClass_value", "movingPrice": 1.1, "priceUnit": 1, "standardPrice": 1.1, "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "material not found",
    "data": []
})


"""
python -m unittest TestAPP.TestStock
"""
class TestStock(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestStock.test_create_success
    """
    def test_create_success(self):
        
        response = self.app.post(
            "/api/stock/create_success",
            json={"materialID": "materialID_value", "plant": "plant_value", "storageLocation": "storageLocation_value", "quantity": 1, "unitOfMeasure": "unitOfMeasure_value", "stockType": "stockType_value", "valuationType": "valuationType_value", "batch": "batch_value", "specialStockIndicator": "specialStockIndicator_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
    "code": 201,
    "message": "success",
    "data": {
        "stockID": "stockID_value"
    }
})


    """
    python -m unittest TestAPP.TestStock.test_update_success
    """
    def test_update_success(self):
        
        response = self.app.patch(
            "/api/stock/update_success",
            json={"stockID": "stockID_value", "materialID": "materialID_value", "plant": "plant_value", "storageLocation": "storageLocation_value", "quantity": 1, "unitOfMeasure": "unitOfMeasure_value", "stockType": "stockType_value", "valuationType": "valuationType_value", "batch": "batch_value", "specialStockIndicator": "specialStockIndicator_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {}
})



    """
    python -m unittest TestAPP.TestStock.test_update_not_found
    """
    def test_update_not_found(self):
        
        response = self.app.patch(
            "/api/stock/update_not_found",
            json={"stockID": "stockID_value", "materialID": "materialID_value", "plant": "plant_value", "storageLocation": "storageLocation_value", "quantity": 1, "unitOfMeasure": "unitOfMeasure_value", "stockType": "stockType_value", "valuationType": "valuationType_value", "batch": "batch_value", "specialStockIndicator": "specialStockIndicator_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "stock not found",
    "data": []
})


    """
    python -m unittest TestAPP.TestStock.test_query_success
    """
    def test_query_success(self):
        
        response = self.app.get(
            "/api/stock/query_success",
            json={"stockID": "stockID_value", "materialID": "materialID_value", "plant": "plant_value", "storageLocation": "storageLocation_value", "quantity": 1, "unitOfMeasure": "unitOfMeasure_value", "stockType": "stockType_value", "valuationType": "valuationType_value", "batch": "batch_value", "specialStockIndicator": "specialStockIndicator_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "stockID": "stockID_value1",
            "materialID": "materialID_value1",
            "plant": "plant_value1",
            "storageLocation": "storageLocation_value1",
            "quantity": 1,
            "unitOfMeasure": "unitOfMeasure_value1",
            "stockType": "stockType_value1",
            "valuationType": "valuationType_value1",
            "batch": "batch_value1",
            "specialStockIndicator": "specialStockIndicator_value1",
            "userID": "userID_value1"
        },
        {
            "stockID": "stockID_value2",
            "materialID": "materialID_value2",
            "plant": "plant_value2",
            "storageLocation": "storageLocation_value2",
            "quantity": 2,
            "unitOfMeasure": "unitOfMeasure_value2",
            "stockType": "stockType_value2",
            "valuationType": "valuationType_value2",
            "batch": "batch_value2",
            "specialStockIndicator": "specialStockIndicator_value2",
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestStock.test_query_not_found
    """
    def test_query_not_found(self):
        
        response = self.app.get(
            "/api/stock/query_not_found",
            json={"stockID": "stockID_value", "materialID": "materialID_value", "plant": "plant_value", "storageLocation": "storageLocation_value", "quantity": 1, "unitOfMeasure": "unitOfMeasure_value", "stockType": "stockType_value", "valuationType": "valuationType_value", "batch": "batch_value", "specialStockIndicator": "specialStockIndicator_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "stock not found",
    "data": []
})


"""
python -m unittest TestAPP.TestGoodsReceipt
"""
class TestGoodsReceipt(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestGoodsReceipt.test_create_success
    """
    def test_create_success(self):
        
        response = self.app.post(
            "/api/goods_receipt/create_success",
            json={"purchaseOrderID": "purchaseOrderID_value", "receiptDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "storageLocation": "storageLocation_value", "batch": "batch_value", "plant": "plant_value", "movementType": "movementType_value", "supplierID": "supplierID_value", "documentDate": "2024/01/01", "postingDate": "2024/01/01", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
    "code": 201,
    "message": "success",
    "data": {
        "goodsReceiptID": "goodsReceiptID_value"
    }
})


    """
    python -m unittest TestAPP.TestGoodsReceipt.test_update_success
    """
    def test_update_success(self):
        
        response = self.app.patch(
            "/api/goods_receipt/update_success",
            json={"goodsReceiptID": "goodsReceiptID_value", "purchaseOrderID": "purchaseOrderID_value", "receiptDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "storageLocation": "storageLocation_value", "batch": "batch_value", "plant": "plant_value", "movementType": "movementType_value", "supplierID": "supplierID_value", "documentDate": "2024/01/01", "postingDate": "2024/01/01", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {}
})



    """
    python -m unittest TestAPP.TestGoodsReceipt.test_update_not_found
    """
    def test_update_not_found(self):
        
        response = self.app.patch(
            "/api/goods_receipt/update_not_found",
            json={"goodsReceiptID": "goodsReceiptID_value", "purchaseOrderID": "purchaseOrderID_value", "receiptDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "storageLocation": "storageLocation_value", "batch": "batch_value", "plant": "plant_value", "movementType": "movementType_value", "supplierID": "supplierID_value", "documentDate": "2024/01/01", "postingDate": "2024/01/01", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "goods receipt not found",
    "data": []
})


    """
    python -m unittest TestAPP.TestGoodsReceipt.test_query_success
    """
    def test_query_success(self):
        
        response = self.app.get(
            "/api/goods_receipt/query_success",
            json={"goodsReceiptID": "goodsReceiptID_value", "purchaseOrderID": "purchaseOrderID_value", "receiptDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "storageLocation": "storageLocation_value", "batch": "batch_value", "plant": "plant_value", "movementType": "movementType_value", "supplierID": "supplierID_value", "documentDate": "2024/01/01", "postingDate": "2024/01/01", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "goodsReceiptID": "goodsReceiptID_value1",
            "purchaseOrderID": "purchaseOrderID_value1",
            "receiptDate": "2024/01/01",
            "materialID": "materialID_value1",
            "quantity": 1,
            "storageLocation": "storageLocation_value1",
            "batch": "batch_value1",
            "plant": "plant_value1",
            "movementType": "movementType_value1",
            "supplierID": "supplierID_value1",
            "documentDate": "2024/01/01",
            "postingDate": "2024/01/01",
            "userID": "userID_value1"
        },
        {
            "goodsReceiptID": "goodsReceiptID_value2",
            "purchaseOrderID": "purchaseOrderID_value2",
            "receiptDate": "2024/02/02",
            "materialID": "materialID_value2",
            "quantity": 2,
            "storageLocation": "storageLocation_value2",
            "batch": "batch_value2",
            "plant": "plant_value2",
            "movementType": "movementType_value2",
            "supplierID": "supplierID_value2",
            "documentDate": "2024/02/02",
            "postingDate": "2024/02/02",
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestGoodsReceipt.test_query_not_found
    """
    def test_query_not_found(self):
        
        response = self.app.get(
            "/api/goods_receipt/query_not_found",
            json={"goodsReceiptID": "goodsReceiptID_value", "purchaseOrderID": "purchaseOrderID_value", "receiptDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "storageLocation": "storageLocation_value", "batch": "batch_value", "plant": "plant_value", "movementType": "movementType_value", "supplierID": "supplierID_value", "documentDate": "2024/01/01", "postingDate": "2024/01/01", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "goods receipt not found",
    "data": []
})


"""
python -m unittest TestAPP.TestPurchaseOrder
"""
class TestPurchaseOrder(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestPurchaseOrder.test_create_success
    """
    def test_create_success(self):
        
        response = self.app.post(
            "/api/purchase_order/create_success",
            json={"supplierID": "supplierID_value", "orderDate": "2024/01/01", "deliveryDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "netPrice": 1.1, "currency": "currency_value", "purchasingGroup": "purchasingGroup_value", "purchasingOrganization": "purchasingOrganization_value", "plant": "plant_value", "paymentTerms": "paymentTerms_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
    "code": 201,
    "message": "success",
    "data": {
        "purchaseOrderID": "purchaseOrderID_value"
    }
})


    """
    python -m unittest TestAPP.TestPurchaseOrder.test_update_success
    """
    def test_update_success(self):
        
        response = self.app.patch(
            "/api/purchase_order/update_success",
            json={"purchaseOrderID": "purchaseOrderID_value", "supplierID": "supplierID_value", "orderDate": "2024/01/01", "deliveryDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "netPrice": 1.1, "currency": "currency_value", "purchasingGroup": "purchasingGroup_value", "purchasingOrganization": "purchasingOrganization_value", "plant": "plant_value", "paymentTerms": "paymentTerms_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {}
})



    """
    python -m unittest TestAPP.TestPurchaseOrder.test_update_not_found
    """
    def test_update_not_found(self):
        
        response = self.app.patch(
            "/api/purchase_order/update_not_found",
            json={"purchaseOrderID": "purchaseOrderID_value", "supplierID": "supplierID_value", "orderDate": "2024/01/01", "deliveryDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "netPrice": 1.1, "currency": "currency_value", "purchasingGroup": "purchasingGroup_value", "purchasingOrganization": "purchasingOrganization_value", "plant": "plant_value", "paymentTerms": "paymentTerms_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "purchase order not found",
    "data": []
})


    """
    python -m unittest TestAPP.TestPurchaseOrder.test_query_success
    """
    def test_query_success(self):
        
        response = self.app.get(
            "/api/purchase_order/query_success",
            json={"purchaseOrderID": "purchaseOrderID_value", "supplierID": "supplierID_value", "orderDate": "2024/01/01", "deliveryDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "netPrice": 1.1, "currency": "currency_value", "purchasingGroup": "purchasingGroup_value", "purchasingOrganization": "purchasingOrganization_value", "plant": "plant_value", "paymentTerms": "paymentTerms_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "purchaseOrderID": "purchaseOrderID_value1",
            "supplierID": "supplierID_value1",
            "orderDate": "2024/01/01",
            "deliveryDate": "2024/01/01",
            "materialID": "materialID_value1",
            "quantity": 1,
            "netPrice": 1.1,
            "currency": "currency_value1",
            "purchasingGroup": "purchasingGroup_value1",
            "purchasingOrganization": "purchasingOrganization_value1",
            "plant": "plant_value1",
            "paymentTerms": "paymentTerms_value1",
            "userID": "userID_value1"
        },
        {
            "purchaseOrderID": "purchaseOrderID_value2",
            "supplierID": "supplierID_value2",
            "orderDate": "2024/02/02",
            "deliveryDate": "2024/02/02",
            "materialID": "materialID_value2",
            "quantity": 2,
            "netPrice": 2.2,
            "currency": "currency_value2",
            "purchasingGroup": "purchasingGroup_value2",
            "purchasingOrganization": "purchasingOrganization_value2",
            "plant": "plant_value2",
            "paymentTerms": "paymentTerms_value2",
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestPurchaseOrder.test_query_not_found
    """
    def test_query_not_found(self):
        
        response = self.app.get(
            "/api/purchase_order/query_not_found",
            json={"purchaseOrderID": "purchaseOrderID_value", "supplierID": "supplierID_value", "orderDate": "2024/01/01", "deliveryDate": "2024/01/01", "materialID": "materialID_value", "quantity": 1, "netPrice": 1.1, "currency": "currency_value", "purchasingGroup": "purchasingGroup_value", "purchasingOrganization": "purchasingOrganization_value", "plant": "plant_value", "paymentTerms": "paymentTerms_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "purchase order not found",
    "data": []
})


"""
python -m unittest TestAPP.TestUser
"""
class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestUser.test_login_success
    """
    def test_login_success(self):
        
        response = self.app.post(
            "/api/user/login_success",
            json={"userID": "userID_value", "password": "password_value"},
            headers={ "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
    "code": 201,
    "message": "success",
    "data": {
        "username": "username_value",
        "role": "role_value"
    }
})



    """
    python -m unittest TestAPP.TestUser.test_login_not_found
    """
    def test_login_not_found(self):
        
        response = self.app.post(
            "/api/user/login_not_found",
            json={"userID": "userID_value", "password": "password_value"},
            headers={ "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "user not found",
    "data": {}
})



    """
    python -m unittest TestAPP.TestUser.test_login_wrong_password
    """
    def test_login_wrong_password(self):
        
        response = self.app.post(
            "/api/user/login_wrong_password",
            json={"userID": "userID_value", "password": "password_value"},
            headers={ "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {
    "code": 401,
    "message": "wrong password",
    "data": {}
})


    """
    python -m unittest TestAPP.TestUser.test_register_success
    """
    def test_register_success(self):
        
        response = self.app.post(
            "/api/user/register_success",
            json={"username": "username_value", "password": "password_value", "role": "role_value"},
            headers={ "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {
        "userID": "userID_value"
    }
})


    """
    python -m unittest TestAPP.TestUser.test_change_password_success
    """
    def test_change_password_success(self):
        
        response = self.app.post(
            "/api/user/change_password_success",
            json={"oldPassword": "old_password_value", "newPassword": "new_password_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": {}
})



    """
    python -m unittest TestAPP.TestUser.test_change_password_wrong
    """
    def test_change_password_wrong(self):
        
        response = self.app.post(
            "/api/user/change_password_wrong",
            json={"oldPassword": "old_password_value", "newPassword": "new_password_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {
    "code": 401,
    "message": "wrong password",
    "data": {}
})


"""
python -m unittest TestAPP.TestDocumentFlow
"""
class TestDocumentFlow(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True


    """
    python -m unittest TestAPP.TestDocumentFlow.test_display_success
    """
    def test_display_success(self):
        
        response = self.app.get(
            "/api/document_flow/display_success/finished",
            json={"PurchaseOrder": "purchaseOrderID_value", "GoodsReceipt": "goodsReceiptID_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "PurchaseOrder": "purchaseOrderID_value1",
            "GoodsReceipt": "goodsReceiptID_value1",
            "userID": "userID_value1"
        },
        {
            "PurchaseOrder": "purchaseOrderID_value2",
            "GoodsReceipt": "goodsReceiptID_value2",
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestDocumentFlow.test_display_success
    """
    def test_display_success(self):
        
        response = self.app.get(
            "/api/document_flow/display_success/unfinished",
            json={"PurchaseOrder": "purchaseOrderID_value", "GoodsReceipt": "goodsReceiptID_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
    "code": 200,
    "message": "success",
    "data": [
        {
            "PurchaseOrder": "purchaseOrderID_value1",
            "GoodsReceipt": "",
            "userID": "userID_value1"
        },
        {
            "PurchaseOrder": "purchaseOrderID_value2",
            "GoodsReceipt": "",
            "userID": "userID_value2"
        }
    ]
})



    """
    python -m unittest TestAPP.TestDocumentFlow.test_display_not_found
    """
    def test_display_not_found(self):
        
        response = self.app.get(
            "/api/document_flow/display_not_found",
            json={"PurchaseOrder": "purchaseOrderID_value", "GoodsReceipt": "goodsReceiptID_value", "userID": "userID_value"},
            headers={ "Authorization": "Bearer <token>",
    "Content-Type": "application/json" }
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {
    "code": 204,
    "message": "document flow not found",
    "data": []
})


if __name__ == '__main__':
    unittest.main()
