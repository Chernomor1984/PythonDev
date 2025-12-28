import os
from pathlib import Path
from FileManager import FileManager
from FileManager import FileMode
from FileManager import FileEncoding
from Logger import Logger

current_path = (
    Path(__file__).resolve().parent  # Путь к папке, содержащей запускающий скрипт
)
os.chdir(current_path)

# Задание 1

logger = Logger("project_root/logs/log.txt")
file_manager = FileManager(logger)
file_manager.make_directory_if_not_exists("project_root/data/raw")
file_manager.make_directory_if_not_exists("project_root/data/processed")
file_manager.make_directory_if_not_exists("project_root/logs")
file_manager.make_directory_if_not_exists("project_root/backups")
file_manager.make_directory_if_not_exists("project_root/output")

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

cyrillic = """Равным образом, высокотехнологичная концепция общественного уклада способствует подготовке и реализации модели развития. Принимая во внимание показатели успешности, сплочённость команды профессионалов требует анализа позиций, занимаемых участниками в отношении поставленных задач. Как принято считать, интерактивные прототипы и по сей день остаются уделом либералов, которые жаждут быть описаны максимально подробно."""

file_manager.write_to_text_file(
    path="project_root/data/raw/utf_file.txt",
    mode=FileMode.a.value,
    encoding=FileEncoding.utf8.value,
    content=cyrillic,
)

file_manager.write_to_text_file(
    path="project_root/data/raw/ascii_file.txt",
    mode=FileMode.a.value,
    encoding=FileEncoding.ascii.value,
    content=lorem_ipsum,
)

file_manager.write_to_text_file(
    path="project_root/data/raw/latin_1_file.txt",
    mode=FileMode.a.value,
    encoding=FileEncoding.latin_1.value,
    content="Hello, World! Ça va? Café £",
)

# Задание 2

text_files_dir_path = "project_root/data/raw"
items = os.listdir(text_files_dir_path)
files = [
    os.path.join(text_files_dir_path, item)
    for item in items
    if os.path.isfile(os.path.join(text_files_dir_path, item))
    and os.path.splitext(item)[1].lower() == ".txt"
]

processed_directory_path = "project_root/data/processed"

for file in files:
    encoding_mode = file_manager.read_file_encoding(file)
    print(f"кодировка файла {file}: {encoding_mode}\n")
    file_name = os.path.basename(file)
    file_name_without_extension, extension = os.path.splitext(file_name)
    processed_file_name = file_name_without_extension + "_processed" + extension
    processed_file_path = os.path.join(processed_directory_path, processed_file_name)

    for line in file_manager.read_file_line_by_line(file, encoding_mode):
        file_manager.write_to_text_file(
            processed_file_path, FileMode.a.value, encoding_mode, line.swapcase()
        )
