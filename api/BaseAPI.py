from dataclasses import dataclass, asdict
import json
from typing import Any
from testInherit import Test

@dataclass
class ResponseBody:
    code: int
    message: str
    body: Any = None

    @property
    def json(self) -> str:
        data = asdict(self)
        if data["body"] is None:
            data["body"] = {}
        return json.dumps(data)