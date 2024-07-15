from flask import Blueprint, jsonify
from model.repositories import DocumentFlowRepository

documentFlowBP = Blueprint("DocumentFlow", __name__)
documentFlowRepository = DocumentFlowRepository()


@documentFlowBP.route("/document_flow")
def test():
    materials = documentFlowRepository.query_one(
        kwargs={"userID": 1, "purchaseOrderID": 1111}
    )
    print(materials.to_dict())
    return jsonify(materials.to_dict())
