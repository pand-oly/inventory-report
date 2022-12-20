import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list:
        if path.endswith(".json"):
            with open(path) as file:
                data = file.read()
                return json.loads(data)

        raise ValueError("Arquivo inválido")
