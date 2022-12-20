from enum import Enum
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class TypeReport(Enum):
    completo = "completo"
    simples = "simples"


class Inventory:
    @staticmethod
    def import_data(path: str, type_report: TypeReport):
        report = ""
        list_products = Inventory.read_file(path)

        if type_report == "simples":
            report = SimpleReport.generate(list_products)
        elif type_report == "completo":
            report = CompleteReport.generate(list_products)

        return report

    @classmethod
    def read_file(cls, path: str):
        if path.endswith(".csv"):
            return CsvImporter.import_data(path)
        elif path.endswith(".json"):
            return JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            return XmlImporter.import_data(path)
        else:
            raise ValueError("Arquivo inválido")
