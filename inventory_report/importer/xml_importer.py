import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str) -> list:
        if path.endswith(".xml"):
            with open(path) as file:
                data = ET.parse(file)
                root = data.getroot()
                list_products = list()

                for elm in root:
                    product = dict()
                    for child in elm:
                        product[child.tag] = child.text

                    list_products.append(product)

                return list_products

        raise ValueError("Arquivo inválido")
