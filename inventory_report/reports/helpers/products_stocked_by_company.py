from collections import Counter


def products_stocked_by_company(list: list):
    companies = [
            item["nome_da_empresa"]
            for item in list
        ]

    quantity_of_company_products = Counter(companies).most_common()

    return quantity_of_company_products
