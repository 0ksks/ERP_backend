from flask import Blueprint, jsonify
from model.repositories import DocumentFlowRepository

documentFlowBP = Blueprint("DocumentFlow", __name__)
documentFlowRepository = DocumentFlowRepository()


class TestClass:
    routeName = "document_flow"

    @staticmethod
    @documentFlowBP.route(f"/{routeName}")
    def test():
        documentFlows = documentFlowRepository.query_one(
            kwargs={"userID": 1, "purchaseOrderID": 1111}
        )
        return jsonify(documentFlows.to_dict())
