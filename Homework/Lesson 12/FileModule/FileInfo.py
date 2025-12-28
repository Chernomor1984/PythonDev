import json
from datetime import datetime


class FileInfo:
    def __init__(
        self,
        name: str,
        path: str,
        size: int,
        creation_date: datetime,
        last_modification_date: datetime,
    ):
        self.name = name
        self.path = path
        self.size = size
        self.creation_date = creation_date
        self.last_modification_date = last_modification_date

    def __str__(self) -> str:
        return (
            f"Файл: {self.name}\n"
            f"Путь: {self.path}\n"
            f"Размер: {self.size} байт\n"
            f"Создан: {self.creation_date.strftime("%d-%m-%Y %H:%M")}\n"
            f"Модифицирован: {self.last_modification_date.strftime("%d-%m-%Y %H:%M")}"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def dict_representation(self) -> dict:
        """
        Преобразует экземпляр класса в словарь
        Returns:
            dict: _description_
        """
        return {
            "name": self.name,
            "path": self.path,
            "size": self.size,
            "creation_date": self.creation_date.isoformat(),
            "last_modification_date": self.last_modification_date.isoformat(),
        }


class FileInfoEncoder(json.JSONEncoder):
    """
    Используется для сериализации экземпляра класса FileInfo в JSON
    """

    def default(self, object: FileInfo):
        if isinstance(object, FileInfo):
            return object.dict_representation()
        return super().default(object)


class FileInfoDecoder:
    """
    Используется для десериализации из JSON в экземпляр класса FileInfo
    """

    @staticmethod
    def decode(json_dictionary: dict) -> FileInfo:
        if (
            "name" in json_dictionary
            and "path" in json_dictionary
            and "size" in json_dictionary
            and "creation_date" in json_dictionary
            and "last_modification_date" in json_dictionary
        ):
            return FileInfo(
                json_dictionary["name"],
                json_dictionary["path"],
                json_dictionary["size"],
                creation_date=datetime.fromisoformat(json_dictionary["creation_date"]),
                last_modification_date=datetime.fromisoformat(
                    json_dictionary["last_modification_date"]
                ),
            )
        else:
            raise TypeError(
                f"FileInfoDecoder error: Insufficient information to deserialize {json_dictionary}"
            )
