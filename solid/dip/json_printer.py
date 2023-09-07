import json
from typing import Dict
from calculator import Printer


class JsonPrinter(Printer):
    def print(self, add, multiply) -> None:
        result: Dict[str, int] = {"add": add, "multiply": multiply}
        with open("result.json", mode="w") as f:
            f.write(json.dumps(result))
