from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    id: str

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj['name'],
            dict_obj['id']
        )
    
    @classmethod
    def from_dict_list(cls, dict_list):
        return [
            Product.from_dict(dict_obj)
            for dict_obj in dict_list
        ]

@dataclass
class JiraProduct:
    jira_id: int
    product: list[Product]

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj['jira_id'],
            Product.from_dict_list(dict_obj['product'])
        )
    
dict_obj=a_dict = {
    "jira_id": 1,
    "product": [
        {
            "name": "aaa",
            "id": 1
        },
        {
            "name": "bbb",
            "id": 2
        }
    ]
}

a_obj = JiraProduct.from_dict(dict_obj)

pass