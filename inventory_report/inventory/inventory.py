import csv
from enum import Enum
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class TypeReport(Enum):
    completo = "completo"
    simples = "simples"


class Inventory:
    @staticmethod
    def import_data(path: str, type: TypeReport):
        with open(path) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            list_products = [product for product in data]

        if type == "simples":
            report = SimpleReport.generate(list_products)
        elif type == "completo":
            report = CompleteReport.generate(list_products)

        return report
