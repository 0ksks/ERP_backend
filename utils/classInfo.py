a = [
    {'className': 'DocumentFlow', 'classAttr': '+documentID:int +userID:int +purchaseOrderID:int +goodsReceiptID:int '},
    {'className': 'GoodsReceipt',
     'classAttr': '+goodsReceiptID:int +userID:int +purchaseOrderID:int +materialID:int +supplierID:int '
                  '+receiptDate:date +quantity:int +stockLocation:string +batch:string +plant:string '
                  '+movementType:string +documentDate:date +postingDate:date '},
    {'className': 'Material',
     'classAttr': '+materialID:int +userID:int +materialName:string +description:string +baseUnit:string '
                  '+materialGroup:string +division:string +grossWeight:float +nettWeight:float +weightUnit:string '
                  '+volume:float +volumeUnit:string +packMaterial:string +availabilityCheck:string '
                  '+transportationGroup:string +loadingGroup:string +mrpType:string +mrpController:string '
                  '+lotSize:string +minimumLotSize:int +plannedDeliveryTime:date +movingPrice:float +priceUnit:string '
                  '+standardPrice:float '},
    {'className': 'PurchaseOrder',
     'classAttr': '+purchaseOrderID:int +userID:int +supplierID:int +materialID:int +orderDate:date '
                  '+deliveryDate:date +quantity:int +netPrice:float +currency:string +purchasingGroup:string '
                  '+purchasingOrganization:string +plant:string +paymentTerms:string '},
    {'className': 'Stock',
     'classAttr': '+StockID:int +userID:int +materialID:int +plant:string +storageLocation:string +quantity:int '
                  '+unitOfMeasure:string +stockType:string +valuationType:string +batch:string '
                  '+specialStockIndicator:string +companyCode:string '},
    {'className': 'Supplier',
     'classAttr': '+supplierID:int +userID:int +supplierName:string +address:string +communicationLang:string '
                  '+taxNumber:int +companyCode:string +reconciliationAcct:string +checkDoubleVoice:string '
                  '+clerkName:string +purchasingOrg:string +orderCurrency:string +paymentTerms:string '
                  '+partnerFunctions:string +streetAddress:string +postalCode:string +country:string +region:string '
                  '+city:string +contactInfo:string '},
    {'className': 'User', 'classAttr': '+userID:int +username:string +password:string +role:string '}]
