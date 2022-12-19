from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.helpers.products_stocked_by_company import products_stocked_by_company


class CompleteReport(SimpleReport):
    # pass
    @staticmethod
    def generate(list: list) -> str:
        simple_report = SimpleReport.generate(list)

        quantity_of_company_products = products_stocked_by_company(list)

        result_format_str = ''
        for company, quantity in quantity_of_company_products:
            result_format_str += f'- {company}: {quantity}\n'

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{result_format_str}"
        )
