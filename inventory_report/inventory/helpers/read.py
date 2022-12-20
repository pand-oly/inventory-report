import csv
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod


class Read(ABC):
    @classmethod
    @abstractmethod
    def read(cls, path: str) -> list:
        raise NotImplementedError


class ReadCsv(Read):
    @classmethod
    def read(cls, path: str) -> list:
        with open(path) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            return [product for product in data]


class ReadJson(Read):
    @classmethod
    def read(cls, path: str) -> list:
        with open(path) as file:
            data = file.read()
            return json.loads(data)


class ReadXml(Read):
    @classmethod
    def read(cls, path: str) -> list:
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
