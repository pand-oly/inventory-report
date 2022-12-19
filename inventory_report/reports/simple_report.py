from datetime import date
# from collections import Counter
from .helpers.products_stocked_by_company import products_stocked_by_company


class SimpleReport:
    @staticmethod
    def generate(list: list):
        today = date.today().strftime("%d-%m-%y")

        oldest_manufacturing = min([
            item["data_de_fabricacao"]
            for item in list
        ])

        nearest_expiration = min([
            item["data_de_validade"]
            for item in list
            if item["data_de_validade"] > today
        ])

        company_with_more_products = products_stocked_by_company(list)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing}\n"
            f"Data de validade mais próxima: {nearest_expiration}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
