from datetime import date
from collections import Counter


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

        companies = [
            item["nome_da_empresa"]
            for item in list
        ]

        company_with_more_products = Counter(companies).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing}\n"
            f"Data de validade mais próxima: {nearest_expiration}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
