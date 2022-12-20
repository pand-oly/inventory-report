from enum import Enum
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.helpers.read import ReadCsv, ReadJson, ReadXml


class TypeReport(Enum):
    completo = "completo"
    simples = "simples"


class Inventory:
    @staticmethod
    def import_data(path: str, type_report: TypeReport):
        list_products = Inventory.read_file(path)

        if type_report == "simples":
            report = SimpleReport.generate(list_products)
        elif type_report == "completo":
            report = CompleteReport.generate(list_products)

        return report

    @classmethod
    def read_file(cls, path: str):
        if path.endswith(".csv"):
            return ReadCsv.read(path)
        elif path.endswith(".json"):
            return ReadJson.read(path)
        elif path.endswith(".xml"):
            return ReadXml.read(path)
        else:
            raise ValueError("Invalid File")
