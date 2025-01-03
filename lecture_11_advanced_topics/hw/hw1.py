"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


>>> assert ColorsEnum.RED == "RED"
>>> assert SizesEnum.XL == "XL"

"""


class SimplifiedEnum(type):
    """Simulates the work enum.py.
    Attention: members must be passed through the __keys class attribute.

    Args:
        *args: Special child class data. Not transmitted directly.
        **kwargs: Special child class data. Not transmitted directly.

    Attributes:
        child_name_plus_child_keys_var: Contains the class name and class attribute.

    """

    def __new__(mcs, name, bases, class_dict):

        cls_instance = super().__new__(mcs, name, bases, class_dict)

        cls_instance.__keys = class_dict[f"_{name}__keys"]
        for key in cls_instance.__keys:
            setattr(cls_instance, key, key)

        return cls_instance

    def __iter__(cls):
        yield from cls.__keys

    def __len__(cls):
        return len(cls.__keys)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
