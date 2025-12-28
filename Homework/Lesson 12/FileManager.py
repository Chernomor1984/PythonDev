import os
from Logger import Logger
from FileSettings import FileEncoding
from FileSettings import FileMode
import chardet


class FileManager:
    def __init__(self, logger: Logger):
        self.__logger = logger

    def make_directory_if_not_exists(self, path: str):
        """
        Создаёт директории, включая промежуточные, если они не существуют
        Иначе выводит в консоль сообщение
        """
        if os.path.exists(path):
            self.__logger.log((f"{path} уже существует"))
        else:
            os.makedirs(path)
            self.__logger.log((f"Создана директория {path}"))

    def write_to_text_file(
        self, path: str, mode: FileMode, encoding: FileEncoding, content: str
    ):
        """
        Создаёт и/или открывает файл по указанному пути с заданной кодировкой
        и производит запись в файл текста
        """
        if encoding not in FileEncoding.get_values():
            self.__logger.log((f"Unsupported file encoding {encoding} at {path}"))
            raise ValueError("Unsupported file encoding")

        if mode not in FileMode.get_values():
            self.__logger.log((f"Unsupported file mode {mode} at {path}"))
            raise ValueError("Unsupported file mode")

        try:
            with open(path, mode=mode, encoding=encoding) as file:
                file.write(content)
                self.__logger.log(f"Данные успешно записаны в {path}")
        except FileNotFoundError as error:
            self.__logger.log((f"Файл {path} не найден: {error}"))
        except PermissionError as error:
            self.__logger.log((f"Доступ к файлу {path} ограничен: {error}"))

    def read_file_encoding(self, path) -> str:
        """
        Читает содержимое текстового файла целиком, возвращая кодировку
        """
        try:
            with open(path, FileMode.rb.value) as file:
                raw_content = file.read()
                detected_data = chardet.detect(raw_content)
                encoding_mode = detected_data["encoding"]
                return encoding_mode
        except FileNotFoundError as error:
            self.__logger.log((f"Файл {path} не найден: {error}"))

    def read_file_line_by_line(self, path: str, encoding: FileEncoding):
        if encoding not in FileEncoding.get_values():
            self.__logger.log((f"Unsupported file encoding {encoding} at {path}"))
            raise ValueError("Unsupported file encoding")

        try:
            with open(path, FileMode.r.value, encoding=encoding) as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError as error:
            self.__logger.log((f"Файл {path} не найден: {error}"))
        except PermissionError as error:
            self.__logger.log((f"Доступ к файлу {path} ограничен: {error}"))
