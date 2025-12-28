import json
from Logger import Logger
from FileSettings import FileMode


class JSONConverter:
    def __init__(self, logger: Logger):
        self.__logger = logger

    def serialize(self, object: dict, path: str):
        """
        Сериализует объект 'object' в jSON файл, расположенный по пути path
        """
        with open(path, FileMode.w.value) as file:
            json.dump(object, file, indent=4)
            self.__logger.log((f"Объект {object} успешно сериализован по пути {path}"))
