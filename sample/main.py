from dataclasses import dataclass
from nesteddataclasses import nested_dataclass


@dataclass
class A:
    aa: int
    ab: str


@nested_dataclass
class B:
    bb: str
    ba: A


data = {'bb': 'str_bb', 'ba': {'aa': 1, 'ab': 'str_ab'}}
b = B(**data)
print('b:', b)
