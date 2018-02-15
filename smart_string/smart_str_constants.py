from enum import Enum


class StrInitInputType(Enum):
    UNKNOWN = 0
    UNICODE_VAL = 1
    UTF_8 = 2
    UTF_16 = 3


class SmartStrException(Exception):
    pass
