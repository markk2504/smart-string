from enum import Enum


class StrRawType(Enum):
    UNDEFINED = 0
    UTF_8 = 1
    UTF_16 = 2


class SmartStrException(Exception):
    pass
