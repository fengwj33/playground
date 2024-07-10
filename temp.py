from dataclasses import dataclass
from typing import List

@dataclass
class Person:
    value_1:str
    value_2:str

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj['value_1'],
            dict_obj['value_2']
        )

@dataclass
class A:
    value:str
    person:Person

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj['value'],
            Person.from_dict(dict_obj['person'])
        )
    
dict_obj={
    'value': 'Value A',
    'person': {
        'value_1': 'pulu pulu',
        'value_2': 'I love Lulu'
    }
}

a_obj = A.from_dict(dict_obj)

pass