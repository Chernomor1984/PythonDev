import os
from datetime import datetime
from FileModule.FileSettings import FileEncoding
from FileModule.FileSettings import FileMode


class Logger:
    def __init__(self, log_file_path: str):
        self.__log_file_path = log_file_path
        log_file_dir_path = os.path.dirname(log_file_path)

        if not os.path.exists(log_file_dir_path):
            os.makedirs(log_file_dir_path)

    def log(self, message: str):
        """
        Логирует текстовое сообщение message в файл, расположенный по пути, указанном в ините
        """
        current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.__write_to_text_file__(
            self.__log_file_path, f"{current_date}\n{message}\n\n"
        )

    def __write_to_text_file__(self, path: str, message: str):
        try:
            with open(
                path, mode=FileMode.a.value, encoding=FileEncoding.utf8.value
            ) as file:
                file.write(message)
        except FileNotFoundError as error:
            raise FileNotFoundError(f"Файл {path} не найден: {error}") from error
        except PermissionError as error:
            raise PermissionError(
                f"Доступ к файлу {path} ограничен: {error}"
            ) from error
