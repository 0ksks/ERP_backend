import json
import unittest

from app import app


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_success(self):
        response = self.app.post(
            "/api/user/login_success",
            json={"userID": 1, "password": "password_value"},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "userID": 1,
        "role": "role_value"
    }
}"""
        print(201)
        print(template)

    def test_login_not_found(self):
        response = self.app.post(
            "/api/user/login_not_found",
            json={"userID": 404, "password": "password_value_404"},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "user not found",
    "data": {}
}"""
        print(200)
        print(template)

    def test_login_wrong_password(self):
        response = self.app.post(
            "/api/user/login_wrong_password",
            json={"userID": 1, "password": "password_value_404"},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 401,
    "message": "wrong password",
    "data": {}
}"""
        print(200)
        print(template)

    def test_register_success(self):
        response = self.app.post(
            "/api/user/register_success",
            json={
                "username": "username_value",
                "password": "password_value",
                "role": "role_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "userID": 1
    }
}"""
        print(201)
        print(template)

    def test_change_password_success(self):
        response = self.app.post(
            "/api/user/change_password_success",
            json={
                "oldPassword": "password_value",
                "newPassword": "new_password_value",
                "userID": 1,
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {}
}"""
        print(201)
        print(template)

    def test_change_password_wrong(self):
        response = self.app.post(
            "/api/user/change_password_wrong",
            json={
                "oldPassword": "old_password_value",
                "newPassword": "new_password_value",
                "userID": 1,
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 401,
    "message": "wrong password",
    "data": {}
}"""
        print(200)
        print(template)


class TestMaterial(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_success(self):
        response = self.app.post(
            "/api/material/create_success",
            json={
                "userID": 1,
                "materialName": "materialName_value2",
                "description": "description_value",
                "baseUnit": "baseUnit_value",
                "materialGroup": "materialGroup_value",
                "division": "division_value",
                "grossWeight": 1.1,
                "nettWeight": 1.1,
                "weightUnit": "weightUnit_value",
                "volume": 1.1,
                "volumeUnit": "volumeUnit_value",
                "packMaterial": "packMaterial_value",
                "availabilityCheck": "availabilityCheck_value",
                "transportationGroup": "transportationGroup_value",
                "loadingGroup": "loadingGroup_value",
                "mrpType": "mrpType_value",
                "mrpController": "mrpController_value",
                "lotSize": "lotSize_value",
                "minimumLotSize": 1,
                "plannedDeliveryTime": "2024/01/01",
                "movingPrice": 1.1,
                "priceUnit": "priceUnit_value",
                "standardPrice": 1.1,
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "materialID": 1
    }
}"""
        print(201)
        print(template)

    def test_update_success(self):
        response = self.app.patch(
            "/api/material/update_success",
            json={
                "materialID": 1,
                "userID": 1,
                "materialName": "materialName_value",
                "description": "description_value",
                "baseUnit": "baseUnit_value",
                "materialGroup": "materialGroup_value",
                "division": "division_value",
                "grossWeight": 1.1,
                "nettWeight": 1.1,
                "weightUnit": "weightUnit_value",
                "volume": 1.1,
                "volumeUnit": "volumeUnit_value",
                "packMaterial": "packMaterial_value",
                "availabilityCheck": "availabilityCheck_value",
                "transportationGroup": "transportationGroup_value",
                "loadingGroup": "loadingGroup_value",
                "mrpType": "mrpType_value",
                "mrpController": "mrpController_value",
                "lotSize": "lotSize_value",
                "minimumLotSize": 1,
                "plannedDeliveryTime": "2024/01/01",
                "movingPrice": 1.1,
                "priceUnit": "priceUnit_value",
                "standardPrice": 1.1,
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": {}
}"""
        print(200)
        print(template)

    def test_update_not_found(self):
        response = self.app.patch(
            "/api/material/update_not_found",
            json={
                "materialID": 404,
                "userID": 404,
                "materialName": "materialName_value_404",
                "description": "description_value_404",
                "baseUnit": "baseUnit_value_404",
                "materialGroup": "materialGroup_value_404",
                "division": "division_value_404",
                "grossWeight": 0.404,
                "nettWeight": 0.404,
                "weightUnit": "weightUnit_value_404",
                "volume": 0.404,
                "volumeUnit": "volumeUnit_value_404",
                "packMaterial": "packMaterial_value_404",
                "availabilityCheck": "availabilityCheck_value_404",
                "transportationGroup": "transportationGroup_value_404",
                "loadingGroup": "loadingGroup_value_404",
                "mrpType": "mrpType_value_404",
                "mrpController": "mrpController_value_404",
                "lotSize": "lotSize_value_404",
                "minimumLotSize": 404,
                "plannedDeliveryTime": "2024/01/01",
                "movingPrice": 0.404,
                "priceUnit": "priceUnit_value_404",
                "standardPrice": 0.404,
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "material not found",
    "data": []
}"""
        print(200)
        print(template)

    def test_query_success(self):
        response = self.app.get(
            "/api/material/query_success",
            # json={"materialID": 1, "userID": 1, "materialName": "materialName_value",
            #       "description": "description_value", "baseUnit": "baseUnit_value",
            #       "materialGroup": "materialGroup_value", "division": "division_value", "grossWeight": 1.1,
            #       "nettWeight": 1.1, "weightUnit": "weightUnit_value", "volume": 1.1, "volumeUnit": "volumeUnit_value",
            #       "packMaterial": "packMaterial_value", "availabilityCheck": "availabilityCheck_value",
            #       "transportationGroup": "transportationGroup_value", "loadingGroup": "loadingGroup_value",
            #       "mrpType": "mrpType_value", "mrpController": "mrpController_value", "lotSize": "lotSize_value",
            #       "minimumLotSize": 1, "plannedDeliveryTime": "2024/01/01", "movingPrice": 1.1,
            #       "priceUnit": "priceUnit_value", "standardPrice": 1.1},
            json={"userID": 1},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "materialID": 1,
            "userID": 1,
            "materialName": "materialName_value1",
            "description": "description_value1",
            "baseUnit": "baseUnit_value1",
            "materialGroup": "materialGroup_value1",
            "division": "division_value1",
            "grossWeight": 1.1,
            "nettWeight": 1.1,
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
            "plannedDeliveryTime": "2024/01/01",
            "movingPrice": 1.1,
            "priceUnit": "priceUnit_value1",
            "standardPrice": 1.1
        },
        {
            "materialID": 2,
            "userID": 2,
            "materialName": "materialName_value2",
            "description": "description_value2",
            "baseUnit": "baseUnit_value2",
            "materialGroup": "materialGroup_value2",
            "division": "division_value2",
            "grossWeight": 2.2,
            "nettWeight": 2.2,
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
            "plannedDeliveryTime": "2024/02/02",
            "movingPrice": 2.2,
            "priceUnit": "priceUnit_value2",
            "standardPrice": 2.2
        }
    ]
}"""
        print(200)
        print(template)

    def test_query_not_found(self):
        response = self.app.get(
            "/api/material/query_not_found",
            json={
                "materialID": 404,
                "userID": 404,
                "materialName": "materialName_value_404",
                "description": "description_value_404",
                "baseUnit": "baseUnit_value_404",
                "materialGroup": "materialGroup_value_404",
                "division": "division_value_404",
                "grossWeight": 0.404,
                "nettWeight": 0.404,
                "weightUnit": "weightUnit_value_404",
                "volume": 0.404,
                "volumeUnit": "volumeUnit_value_404",
                "packMaterial": "packMaterial_value_404",
                "availabilityCheck": "availabilityCheck_value_404",
                "transportationGroup": "transportationGroup_value_404",
                "loadingGroup": "loadingGroup_value_404",
                "mrpType": "mrpType_value_404",
                "mrpController": "mrpController_value_404",
                "lotSize": "lotSize_value_404",
                "minimumLotSize": 404,
                "plannedDeliveryTime": "2024/01/01",
                "movingPrice": 0.404,
                "priceUnit": "priceUnit_value_404",
                "standardPrice": 0.404,
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "material not found",
    "data": []
}"""
        print(200)
        print(template)


class TestStock(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_success(self):
        response = self.app.post(
            "/api/stock/create_success",
            json={
                "userID": 1,
                "materialID": 1,
                "plant": "plant_value",
                "storageLocation": "storageLocation_value",
                "quantity": 1,
                "unitOfMeasure": "unitOfMeasure_value",
                "stockType": "stockType_value",
                "valuationType": "valuationType_value",
                "batch": "batch_value",
                "specialStockIndicator": "specialStockIndicator_value",
                "companyCode": "companyCode_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "stockID": 1
    }
}"""
        print(201)
        print(template)

    def test_update_success(self):
        response = self.app.patch(
            "/api/stock/update_success",
            json={
                "stockID": 1,
                "userID": 1,
                "materialID": 1,
                "plant": "plant_value",
                "storageLocation": "storageLocation_value",
                "quantity": 1,
                "unitOfMeasure": "unitOfMeasure_value",
                "stockType": "stockType_value",
                "valuationType": "valuationType_value",
                "batch": "batch_value",
                "specialStockIndicator": "specialStockIndicator_value",
                "companyCode": "companyCode_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": {}
}"""
        print(200)
        print(template)

    def test_update_not_found(self):
        response = self.app.patch(
            "/api/stock/update_not_found",
            json={
                "stockID": 404,
                "userID": 404,
                "materialID": 404,
                "plant": "plant_value_404",
                "storageLocation": "storageLocation_value_404",
                "quantity": 404,
                "unitOfMeasure": "unitOfMeasure_value_404",
                "stockType": "stockType_value_404",
                "valuationType": "valuationType_value_404",
                "batch": "batch_value_404",
                "specialStockIndicator": "specialStockIndicator_value_404",
                "companyCode": "companyCode_value_404",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "stock not found",
    "data": []
}"""
        print(200)
        print(template)

    def test_query_success(self):
        response = self.app.get(
            "/api/stock/query_success",
            json={
                "stockID": 1,
                "userID": 1,
                "materialID": 1,
                "plant": "plant_value",
                "storageLocation": "storageLocation_value",
                "quantity": 1,
                "unitOfMeasure": "unitOfMeasure_value",
                "stockType": "stockType_value",
                "valuationType": "valuationType_value",
                "batch": "batch_value",
                "specialStockIndicator": "specialStockIndicator_value",
                "companyCode": "companyCode_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "stockID": 1,
            "userID": 1,
            "materialID": 1,
            "plant": "plant_value1",
            "storageLocation": "storageLocation_value1",
            "quantity": 1,
            "unitOfMeasure": "unitOfMeasure_value1",
            "stockType": "stockType_value1",
            "valuationType": "valuationType_value1",
            "batch": "batch_value1",
            "specialStockIndicator": "specialStockIndicator_value1",
            "companyCode": "companyCode_value1"
        },
        {
            "stockID": 2,
            "userID": 2,
            "materialID": 2,
            "plant": "plant_value2",
            "storageLocation": "storageLocation_value2",
            "quantity": 2,
            "unitOfMeasure": "unitOfMeasure_value2",
            "stockType": "stockType_value2",
            "valuationType": "valuationType_value2",
            "batch": "batch_value2",
            "specialStockIndicator": "specialStockIndicator_value2",
            "companyCode": "companyCode_value2"
        }
    ]
}"""
        print(200)
        print(template)

    def test_query_not_found(self):
        response = self.app.get(
            "/api/stock/query_not_found",
            json={
                "stockID": 404,
                "userID": 404,
                "materialID": 404,
                "plant": "plant_value_404",
                "storageLocation": "storageLocation_value_404",
                "quantity": 404,
                "unitOfMeasure": "unitOfMeasure_value_404",
                "stockType": "stockType_value_404",
                "valuationType": "valuationType_value_404",
                "batch": "batch_value_404",
                "specialStockIndicator": "specialStockIndicator_value_404",
                "companyCode": "companyCode_value_404",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "stock not found",
    "data": []
}"""
        print(200)
        print(template)


class TestSupplier(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_success(self):
        response = self.app.post(
            "/api/supplier/create_success",
            json={
                "userID": 1,
                "supplierName": "supplierName_value",
                "address": "address_value",
                "communicationLang": "communicationLang_value",
                "taxNumber": 1,
                "companyCode": "companyCode_value",
                "reconciliationAcct": "reconciliationAcct_value",
                "checkDoubleVoice": "checkDoubleVoice_value",
                "clerkName": "clerkName_value",
                "purchasingOrg": "purchasingOrg_value",
                "orderCurrency": "orderCurrency_value",
                "paymentTerms": "paymentTerms_value",
                "partnerFunctions": "partnerFunctions_value",
                "streetAddress": "streetAddress_value",
                "postalCode": "postalCode_value",
                "country": "country_value",
                "region": "region_value",
                "city": "city_value",
                "contactInfo": "contactInfo_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "supplierID": 1
    }
}"""
        print(201)
        print(template)

    def test_update_success(self):
        response = self.app.patch(
            "/api/supplier/update_success",
            json={
                "supplierID": 1,
                "userID": 1,
                "supplierName": "supplierName_value",
                "address": "address_value",
                "communicationLang": "communicationLang_value",
                "taxNumber": 1,
                "companyCode": "companyCode_value",
                "reconciliationAcct": "reconciliationAcct_value",
                "checkDoubleVoice": "checkDoubleVoice_value",
                "clerkName": "clerkName_value",
                "purchasingOrg": "purchasingOrg_value",
                "orderCurrency": "orderCurrency_value",
                "paymentTerms": "paymentTerms_value",
                "partnerFunctions": "partnerFunctions_value",
                "streetAddress": "streetAddress_value",
                "postalCode": "postalCode_value",
                "country": "country_value",
                "region": "region_value",
                "city": "city_value",
                "contactInfo": "contactInfo_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": {}
}"""
        print(200)
        print(template)

    def test_update_not_found(self):
        response = self.app.patch(
            "/api/supplier/update_not_found",
            json={
                "supplierID": 404,
                "userID": 404,
                "supplierName": "supplierName_value_404",
                "address": "address_value_404",
                "communicationLang": "communicationLang_value_404",
                "taxNumber": 404,
                "companyCode": "companyCode_value_404",
                "reconciliationAcct": "reconciliationAcct_value_404",
                "checkDoubleVoice": "checkDoubleVoice_value_404",
                "clerkName": "clerkName_value_404",
                "purchasingOrg": "purchasingOrg_value_404",
                "orderCurrency": "orderCurrency_value_404",
                "paymentTerms": "paymentTerms_value_404",
                "partnerFunctions": "partnerFunctions_value_404",
                "streetAddress": "streetAddress_value_404",
                "postalCode": "postalCode_value_404",
                "country": "country_value_404",
                "region": "region_value_404",
                "city": "city_value_404",
                "contactInfo": "contactInfo_value_404",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "supplier not found",
    "data": []
}"""
        print(200)
        print(template)

    def test_query_success(self):
        response = self.app.get(
            "/api/supplier/query_success",
            json={
                "supplierID": 1,
                "userID": 1,
                "supplierName": "supplierName_value",
                "address": "address_value",
                "communicationLang": "communicationLang_value",
                "taxNumber": 1,
                "companyCode": "companyCode_value",
                "reconciliationAcct": "reconciliationAcct_value",
                "checkDoubleVoice": "checkDoubleVoice_value",
                "clerkName": "clerkName_value",
                "purchasingOrg": "purchasingOrg_value",
                "orderCurrency": "orderCurrency_value",
                "paymentTerms": "paymentTerms_value",
                "partnerFunctions": "partnerFunctions_value",
                "streetAddress": "streetAddress_value",
                "postalCode": "postalCode_value",
                "country": "country_value",
                "region": "region_value",
                "city": "city_value",
                "contactInfo": "contactInfo_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "supplierID": 1,
            "userID": 1,
            "supplierName": "supplierName_value1",
            "address": "address_value1",
            "communicationLang": "communicationLang_value1",
            "taxNumber": 1,
            "companyCode": "companyCode_value1",
            "reconciliationAcct": "reconciliationAcct_value1",
            "checkDoubleVoice": "checkDoubleVoice_value1",
            "clerkName": "clerkName_value1",
            "purchasingOrg": "purchasingOrg_value1",
            "orderCurrency": "orderCurrency_value1",
            "paymentTerms": "paymentTerms_value1",
            "partnerFunctions": "partnerFunctions_value1",
            "streetAddress": "streetAddress_value1",
            "postalCode": "postalCode_value1",
            "country": "country_value1",
            "region": "region_value1",
            "city": "city_value1",
            "contactInfo": "contactInfo_value1"
        },
        {
            "supplierID": 2,
            "userID": 2,
            "supplierName": "supplierName_value2",
            "address": "address_value2",
            "communicationLang": "communicationLang_value2",
            "taxNumber": 2,
            "companyCode": "companyCode_value2",
            "reconciliationAcct": "reconciliationAcct_value2",
            "checkDoubleVoice": "checkDoubleVoice_value2",
            "clerkName": "clerkName_value2",
            "purchasingOrg": "purchasingOrg_value2",
            "orderCurrency": "orderCurrency_value2",
            "paymentTerms": "paymentTerms_value2",
            "partnerFunctions": "partnerFunctions_value2",
            "streetAddress": "streetAddress_value2",
            "postalCode": "postalCode_value2",
            "country": "country_value2",
            "region": "region_value2",
            "city": "city_value2",
            "contactInfo": "contactInfo_value2"
        }
    ]
}"""
        print(200)
        print(template)

    def test_query_not_found(self):
        response = self.app.get(
            "/api/supplier/query_not_found",
            json={
                "supplierID": 404,
                "userID": 404,
                "supplierName": "supplierName_value_404",
                "address": "address_value_404",
                "communicationLang": "communicationLang_value_404",
                "taxNumber": 404,
                "companyCode": "companyCode_value_404",
                "reconciliationAcct": "reconciliationAcct_value_404",
                "checkDoubleVoice": "checkDoubleVoice_value_404",
                "clerkName": "clerkName_value_404",
                "purchasingOrg": "purchasingOrg_value_404",
                "orderCurrency": "orderCurrency_value_404",
                "paymentTerms": "paymentTerms_value_404",
                "partnerFunctions": "partnerFunctions_value_404",
                "streetAddress": "streetAddress_value_404",
                "postalCode": "postalCode_value_404",
                "country": "country_value_404",
                "region": "region_value_404",
                "city": "city_value_404",
                "contactInfo": "contactInfo_value_404",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "supplier not found",
    "data": []
}"""
        print(200)
        print(template)


class TestPurchaseOrder(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_success(self):
        response = self.app.post(
            "/api/purchase_order/create_success",
            json={
                "userID": 1,
                "supplierID": 1,
                "stockID": 1,
                "orderDate": "2024/01/01",
                "deliveryDate": "2024/01/01",
                "quantity": 1,
                "netPrice": 1.1,
                "currency": "currency_value",
                "purchasingGroup": "purchasingGroup_value",
                "purchasingOrganization": "purchasingOrganization_value",
                "plant": "plant_value",
                "paymentTerms": "paymentTerms_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "purchaseOrderID": 1
    }
}"""
        print(201)
        print(template)

    def test_update_success(self):
        response = self.app.patch(
            "/api/purchase_order/update_success",
            json={
                "purchaseOrderID": 1,
                "userID": 1,
                "supplierID": 1,
                "stockID": 1,
                "orderDate": "2024/01/01",
                "deliveryDate": "2024/01/01",
                "quantity": 1,
                "netPrice": 1.1,
                "currency": "currency_value",
                "purchasingGroup": "purchasingGroup_value",
                "purchasingOrganization": "purchasingOrganization_value",
                "plant": "plant_value",
                "paymentTerms": "paymentTerms_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": {}
}"""
        print(200)
        print(template)

    def test_update_not_found(self):
        response = self.app.patch(
            "/api/purchase_order/update_not_found",
            json={
                "purchaseOrderID": 404,
                "userID": 404,
                "supplierID": 404,
                "stockID": 404,
                "orderDate": "2024/01/01",
                "deliveryDate": "2024/01/01",
                "quantity": 404,
                "netPrice": 0.404,
                "currency": "currency_value_404",
                "purchasingGroup": "purchasingGroup_value_404",
                "purchasingOrganization": "purchasingOrganization_value_404",
                "plant": "plant_value_404",
                "paymentTerms": "paymentTerms_value_404",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "purchase order not found",
    "data": []
}"""
        print(200)
        print(template)

    def test_query_success(self):
        response = self.app.get(
            "/api/purchase_order/query_success",
            json={
                "purchaseOrderID": 1,
                "userID": 1,
                "supplierID": 1,
                "stockID": 1,
                "orderDate": "2024/01/01",
                "deliveryDate": "2024/01/01",
                "quantity": 1,
                "netPrice": 1.1,
                "currency": "currency_value",
                "purchasingGroup": "purchasingGroup_value",
                "purchasingOrganization": "purchasingOrganization_value",
                "plant": "plant_value",
                "paymentTerms": "paymentTerms_value",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "purchaseOrderID": 1,
            "userID": 1,
            "supplierID": 1,
            "stockID": 1,
            "orderDate": "2024/01/01",
            "deliveryDate": "2024/01/01",
            "quantity": 1,
            "netPrice": 1.1,
            "currency": "currency_value1",
            "purchasingGroup": "purchasingGroup_value1",
            "purchasingOrganization": "purchasingOrganization_value1",
            "plant": "plant_value1",
            "paymentTerms": "paymentTerms_value1"
        },
        {
            "purchaseOrderID": 2,
            "userID": 2,
            "supplierID": 2,
            "stockID": 2,
            "orderDate": "2024/02/02",
            "deliveryDate": "2024/02/02",
            "quantity": 2,
            "netPrice": 2.2,
            "currency": "currency_value2",
            "purchasingGroup": "purchasingGroup_value2",
            "purchasingOrganization": "purchasingOrganization_value2",
            "plant": "plant_value2",
            "paymentTerms": "paymentTerms_value2"
        }
    ]
}"""
        print(200)
        print(template)

    def test_query_not_found(self):
        response = self.app.get(
            "/api/purchase_order/query_not_found",
            json={
                "purchaseOrderID": 404,
                "userID": 404,
                "supplierID": 404,
                "stockID": 404,
                "orderDate": "2024/01/01",
                "deliveryDate": "2024/01/01",
                "quantity": 404,
                "netPrice": 0.404,
                "currency": "currency_value_404",
                "purchasingGroup": "purchasingGroup_value_404",
                "purchasingOrganization": "purchasingOrganization_value_404",
                "plant": "plant_value_404",
                "paymentTerms": "paymentTerms_value_404",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "purchase order not found",
    "data": []
}"""
        print(200)
        print(template)


class TestGoodsReceipt(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_success(self):
        response = self.app.post(
            "/api/goods_receipt/create_success",
            json={
                "userID": 1,
                "purchaseOrderID": 1,
                "materialID": 1,
                "supplierID": 1,
                "receiptDate": "2024/01/01",
                "quantity": 1,
                "stockLocation": "stockLocation_value",
                "batch": "batch_value",
                "plant": "plant_value",
                "movementType": "movementType_value",
                "documentDate": "2024/01/01",
                "postingDate": "2024/01/01",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 201,
    "message": "success",
    "data": {
        "goodsReceiptID": 1
    }
}"""
        print(201)
        print(template)

    def test_update_success(self):
        response = self.app.patch(
            "/api/goods_receipt/update_success",
            json={
                "goodsReceiptID": 1,
                "userID": 1,
                "purchaseOrderID": 1,
                "materialID": 1,
                "supplierID": 1,
                "receiptDate": "2024/01/01",
                "quantity": 1,
                "stockLocation": "stockLocation_value",
                "batch": "batch_value",
                "plant": "plant_value",
                "movementType": "movementType_value",
                "documentDate": "2024/01/01",
                "postingDate": "2024/01/01",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": {}
}"""
        print(200)
        print(template)

    def test_update_not_found(self):
        response = self.app.patch(
            "/api/goods_receipt/update_not_found",
            json={
                "goodsReceiptID": 404,
                "userID": 404,
                "purchaseOrderID": 404,
                "materialID": 404,
                "supplierID": 404,
                "receiptDate": "2024/01/01",
                "quantity": 404,
                "stockLocation": "stockLocation_value_404",
                "batch": "batch_value_404",
                "plant": "plant_value_404",
                "movementType": "movementType_value_404",
                "documentDate": "2024/01/01",
                "postingDate": "2024/01/01",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "goods receipt not found",
    "data": []
}"""
        print(200)
        print(template)

    def test_query_success(self):
        response = self.app.get(
            "/api/goods_receipt/query_success",
            json={
                "goodsReceiptID": 1,
                "userID": 1,
                "purchaseOrderID": 1,
                "materialID": 1,
                "supplierID": 1,
                "receiptDate": "2024/01/01",
                "quantity": 1,
                "stockLocation": "stockLocation_value",
                "batch": "batch_value",
                "plant": "plant_value",
                "movementType": "movementType_value",
                "documentDate": "2024/01/01",
                "postingDate": "2024/01/01",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "goodsReceiptID": 1,
            "userID": 1,
            "purchaseOrderID": 1,
            "materialID": 1,
            "supplierID": 1,
            "receiptDate": "2024/01/01",
            "quantity": 1,
            "stockLocation": "stockLocation_value1",
            "batch": "batch_value1",
            "plant": "plant_value1",
            "movementType": "movementType_value1",
            "documentDate": "2024/01/01",
            "postingDate": "2024/01/01"
        },
        {
            "goodsReceiptID": 2,
            "userID": 2,
            "purchaseOrderID": 2,
            "materialID": 2,
            "supplierID": 2,
            "receiptDate": "2024/02/02",
            "quantity": 2,
            "stockLocation": "stockLocation_value2",
            "batch": "batch_value2",
            "plant": "plant_value2",
            "movementType": "movementType_value2",
            "documentDate": "2024/02/02",
            "postingDate": "2024/02/02"
        }
    ]
}"""
        print(200)
        print(template)

    def test_query_not_found(self):
        response = self.app.get(
            "/api/goods_receipt/query_not_found",
            json={
                "goodsReceiptID": 404,
                "userID": 404,
                "purchaseOrderID": 404,
                "materialID": 404,
                "supplierID": 404,
                "receiptDate": "2024/01/01",
                "quantity": 404,
                "stockLocation": "stockLocation_value_404",
                "batch": "batch_value_404",
                "plant": "plant_value_404",
                "movementType": "movementType_value_404",
                "documentDate": "2024/01/01",
                "postingDate": "2024/01/01",
            },
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "goods receipt not found",
    "data": []
}"""
        print(200)
        print(template)


class TestDocumentFlow(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_display_success_finished(self):
        response = self.app.get(
            "/api/document_flow/display_success/finished",
            json={"purchaseOrderID": 1, "goodsReceiptID": 1, "userID": 1},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "purchaseOrderID": 1,
            "goodsReceiptID": 1,
            "userID": 1
        },
        {
            "purchaseOrderID": 2,
            "goodsReceiptID": 2,
            "userID": 2
        }
    ]
}"""
        print(200)
        print(template)

    def test_display_success_unfinished(self):
        response = self.app.get(
            "/api/document_flow/display_success/unfinished",
            json={"purchaseOrderID": 1, "goodsReceiptID": 1, "userID": 1},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 200,
    "message": "success",
    "data": [
        {
            "purchaseOrderID": 1,
            "goodsReceiptID": 1,
            "userID": 1
        },
        {
            "purchaseOrderID": 2,
            "goodsReceiptID": 2,
            "userID": 2
        }
    ]
}"""
        print(200)
        print(template)

    def test_display_not_found(self):
        response = self.app.get(
            "/api/document_flow/display_not_found",
            json={"purchaseOrderID": 404, "goodsReceiptID": 404, "userID": 404},
            headers={"Content-Type": "application/json"},
        )
        print("real data")
        print(response.status_code)
        print(json.dumps(json.loads(response.data.decode("utf-8")), indent=4))
        print("template data")
        template = """{
    "code": 404,
    "message": "document flow not found",
    "data": []
}"""
        print(200)
        print(template)


if __name__ == "__main__":
    unittest.main()
