from flask import Blueprint, jsonify
from model.repositories import DocumentFlowRepository

documentFlowBP = Blueprint("DocumentFlow", __name__)
documentFlowRepository = DocumentFlowRepository()


@documentFlowBP.route("/document_flow")
def test():
    documentFlows = documentFlowRepository.query_one(
        kwargs={"userID": 1, "purchaseOrderID": 1111}
    )
    return jsonify(documentFlows.to_dict())
