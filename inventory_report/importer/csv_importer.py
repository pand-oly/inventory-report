import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list:
        if path.endswith(".csv"):
            with open(path) as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                return [product for product in data]

        raise ValueError("Arquivo inválido")
