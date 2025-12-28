import os
from Utils import Logger
from .FileSettings import FileEncoding
from .FileSettings import FileMode
import chardet
import shutil
from datetime import datetime


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
        и производит запись текста в файл
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
        """
        Читает файл с заданной кодировкой по пути path построчно
        """
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

    def read_file(self, path: str, encoding: FileEncoding) -> str:
        """
        Читает файл с заданной кодировкой по пути path целиком, возвращая строку
        """
        if encoding not in FileEncoding.get_values():
            self.__logger.log((f"Unsupported file encoding {encoding} at {path}"))
            raise ValueError("Unsupported file encoding")

        try:
            with open(path, FileMode.r.value, encoding=encoding) as file:
                content = file.read()
                return content
        except FileNotFoundError as error:
            self.__logger.log((f"Файл {path} не найден: {error}"))
        except PermissionError as error:
            self.__logger.log((f"Доступ к файлу {path} ограничен: {error}"))

    def make_zip_archive(self, source_path: str, destination_path: str):
        """
        Создаёт zip архив папки
        Args:
            source_path (str): Путь к папке, которую нужно архивировать
            destination_path (str): Путь к папке, где будет лежать архив с именем backup_YYYYMMDD.zip
        """
        formatted_current_date = datetime.now().strftime("%Y%m%d")
        output_file_name = f"backup_{formatted_current_date}"
        output_path = os.path.join(destination_path, output_file_name)
        archive_from = os.path.dirname(source_path)
        archive_to = os.path.basename(source_path)
        shutil.make_archive(output_path, "zip", archive_from, archive_to)
        self.__logger.log((f"{output_path}.zip создан"))

    def unzip_archive(self, zip_file_path: str, extract_dir_path: str):
        """
        Разархивирует zip архив
        Args:
            zip_file_path (str): Путь к zip архиву
            extract_path (str): Путь к директории с разархивированными файлами
        """
        try:
            shutil.unpack_archive(zip_file_path, extract_dir_path, "zip")
            self.__logger.log(
                (f"{zip_file_path}.zip успешно разархивирован в {extract_dir_path}")
            )
        except shutil.ReadError as error:
            self.__logger.log((f"Can't read file at {zip_file_path}"))
        except Exception as error:
            self.__logger.log((f"Unzip error: {error}"))

    def get_file_paths_at_dir(self, dir_path: str, file_extension: str) -> list[str]:
        """
        Считывает контент в dir_path и возвращает
        абсолютные пути к файлам в ней с расширением file_extension
        Args:
            dir_path (str): Путь к директории, в которой осуществляется поиск файлов
            file_extension (str): Расширение искомых файлов

        Returns:
            list[str]: сортированный по возрастанию список абсолютных путей к файлам
        """
        items = os.listdir(dir_path)
        items.sort()
        file_paths = [
            os.path.join(dir_path, item)
            for item in items
            if os.path.isfile(os.path.join(dir_path, item))
            and os.path.splitext(item)[1].lower() == f".{file_extension}"
        ]
        return file_paths
