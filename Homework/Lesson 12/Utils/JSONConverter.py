import json
from Utils.Logger import Logger
from FileModule.FileSettings import FileMode


class JSONConverter:
    def __init__(self, logger: Logger):
        self.__logger = logger

    def serialize(self, object: dict, path: str):
        """
        Сериализует объект 'object' в jSON файл, расположенный по пути path

        Args:
            object (_type_): сериализуемый объект
            path (str): Путь к json файлу
        """
        with open(path, FileMode.w.value) as file:
            json.dump(object, file, indent=4)
            self.__logger.log((f"Объект {object} успешно сериализован по пути {path}"))

    def custom_serialize(self, object, encoder, path: str):
        """
        Сериализует объект в jSON файл, расположенный по пути path, используя кастомный encoder

        Args:
            object (_type_): сериализуемый объект
            encoder (_type_): класс, реализующий кастомную сериализацию
            path (str): Путь к json файлу
        """
        with open(path, FileMode.w.value) as file:
            json.dump(object, file, cls=encoder, indent=4)
            self.__logger.log((f"Объект {object} успешно сериализован по пути {path}"))

    def custom_deserialize(self, path: str, object_decoder):
        """
        Десериализует данные из файла, используя кастомный десериализатор
        Args:
            path (str): Путь к json файлу
            object_decoder (_type_): Метод с кастомной реализацией десериализации
        """
        with open(path, FileMode.r.value) as file:
            file_info_list = json.load(file, object_hook=object_decoder)
            return file_info_list
