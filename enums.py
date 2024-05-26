from enum import Enum


class Gender(Enum):
    MALE = "m"
    FEMALE = "f"


class Direction(Enum):
    LEFT = "l"
    RIGHT = "r"
    FORWARD = "f"
    UP = "u"
    DOWN = "d"


class Room(Enum):
    CELL = "cell"
    NURSE_OFFICE = "nurses office"


class DRUG(Enum):
    VALIUM_SEDATIVE = "v"
    BENADRYL = "b"
    LEECH_SALIVA = "ls"
