import importlib
import json
from dataclasses import dataclass, asdict
from typing import Any, TypeVar, Type

import stringcase
from flask import Blueprint, request
from stringcase import snakecase

from model.repositories import BaseRepository

ResponseData = TypeVar('ResponseData', dict[str, Any], list[dict[str, Any]])


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
        return Response(code=204, message=f"{entity} not found", data=[]).json, 204

    @staticmethod
    def query_success(data: ResponseData):
        return Response(code=200, message="success", data=data).json, 200


class Controller:
    def __init__(self, entityName: str, repository: Type[BaseRepository], blueprint: Blueprint):
        self.repository = repository
        self.blueprint = blueprint
        self.entityName = entityName
        self.register_routes()

    def register_routes(self):
        self.blueprint.route('/create_success', methods=['POST'])(self.create)
        # self.blueprint.route('/update', methods=['PUT'])(self.update)
        # self.blueprint.route('/query', methods=['GET'])(self.query)

    def create(self):
        data = request.json
        instance = self.repository.create(kwargs=data)
        entityIDKey = stringcase.lowercase(self.entityName) + "ID"
        entityIDValue = instance.to_dict()[entityIDKey]
        return Response.create_success({entityIDKey: entityIDValue})

    # def update(self):
    #     data = request.json
    #     ID = data.get('id')
    #     if not ID:
    #         return jsonify({"error": "ID is required"}), 400
    #     result = self.repository.update(ID, data)
    #     if result:
    #         return jsonify(result), 200
    #     else:
    #         return jsonify({"error": "Entity not found"}), 404
    # 
    # def query(self):
    #     filters = request.args.to_dict()
    #     results = self.repository.query_list(filters)
    #     return jsonify(results), 200

    @classmethod
    def register(cls, entityName: str):
        module = importlib.import_module("model.repositories")
        EntityRepository = getattr(module, f"{entityName}Repository")
        EntityBlueprint = Blueprint(entityName, __name__, url_prefix=f"/api/{snakecase(entityName)}")
        return cls(entityName, EntityRepository(), EntityBlueprint).blueprint
