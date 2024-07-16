import json
from dataclasses import dataclass, asdict
from typing import Any, TypeVar, Type

from flask import request, Blueprint

from model.repositories import BaseRepository

ResponseData = TypeVar('ResponseData', dict[str, Any], list[dict[str, Any]])


@dataclass
class ResponseBody:
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
        return ResponseBody(code=201, message="success", data=data)

    @staticmethod
    def update_success():
        return ResponseBody(code=200, message="success", data={})

    @staticmethod
    def not_found(entity: str):
        return ResponseBody(code=204, message=f"{entity} not found", data=[])

    @staticmethod
    def query_success(data: ResponseData):
        return ResponseBody(code=200, message="success", data=data)


class BaseController:
    def __init__(self, repository: Type[BaseRepository], blueprint: Blueprint):
        self.repository = repository
        self.blueprint = blueprint
        self.register_routes()

    def register_routes(self):
        self.blueprint.route('/create', methods=['POST'])(self.create)
        self.blueprint.route('/update', methods=['PUT'])(self.update)
        self.blueprint.route('/query', methods=['GET'])(self.query)

    def create(self):
        data = request.json
        result = self.repository.create(data)
        return result, 201

    def update(self):
        data = request.json
        id = data.get('id')
        if not id:
            return ({"error": "ID is required"}), 400
        result = self.repository.update(id, data)
        if result:
            return result, 200
        else:
            return ({"error": "Entity not found"}), 404

    def query(self):
        filters = request.args.to_dict()
        results = self.repository.query_list(filters)
        return results, 200
