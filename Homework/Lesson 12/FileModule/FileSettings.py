from enum import Enum


class FileEncoding(Enum):
    utf8 = "utf-8"
    ascii = "ascii"
    latin_1 = "ISO-8859-1"

    @staticmethod
    def get_values() -> set:
        return set(item.value for item in FileEncoding)


class FileMode(Enum):
    r = "r"
    w = "w"
    a = "a"
    b = "b"
    rp = "r+"
    wp = "w+"
    ap = "a+"
    rb = "rb"
    wb = "wb"
    ab = "ab"

    @staticmethod
    def get_values() -> set:
        return set(item.value for item in FileMode)
