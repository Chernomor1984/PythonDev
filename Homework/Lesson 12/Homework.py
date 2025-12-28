import os
from pathlib import Path
from FileModule.FileManager import FileManager
from FileModule.FileSettings import FileEncoding
from FileModule.FileSettings import FileMode
from FileModule.FileInfo import FileInfo
from FileModule.FileInfo import FileInfoEncoder
from FileModule.FileInfo import FileInfoDecoder
from Utils.Logger import Logger
from Utils.JSONConverter import JSONConverter
from Utils.FileInfoJSONSchemaValidator import FileInfoJSONSchemaValidator
import time
from datetime import datetime, timezone

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
    mode=FileMode.w.value,
    encoding=FileEncoding.utf8.value,
    content=cyrillic,
)

file_manager.write_to_text_file(
    path="project_root/data/raw/ascii_file.txt",
    mode=FileMode.w.value,
    encoding=FileEncoding.ascii.value,
    content=lorem_ipsum,
)

file_manager.write_to_text_file(
    path="project_root/data/raw/latin_1_file.txt",
    mode=FileMode.w.value,
    encoding=FileEncoding.latin_1.value,
    content="Hello, World! Ça va? Café £",
)

# Задание 2
files = file_manager.get_file_paths_at_dir("project_root/data/raw", "txt")
processed_directory_path = "project_root/data/processed"

for file in files:
    encoding_mode = file_manager.read_file_encoding(file)
    file_name = os.path.basename(file)
    file_name_without_extension, extension = os.path.splitext(file_name)
    processed_file_name = file_name_without_extension + "_processed" + extension
    processed_file_path = os.path.join(processed_directory_path, processed_file_name)

    for line in file_manager.read_file_line_by_line(file, encoding_mode):
        file_manager.write_to_text_file(
            processed_file_path, FileMode.a.value, encoding_mode, line.swapcase()
        )

processed_files = file_manager.get_file_paths_at_dir(processed_directory_path, "txt")
data = []
for file, processed_file in zip(files, processed_files):
    file_name = os.path.basename(processed_file)
    file_size_bytes = os.path.getsize(processed_file)
    last_modification_date = time.ctime(os.path.getmtime(processed_file))
    encoding_mode = file_manager.read_file_encoding(file)
    raw_content = file_manager.read_file(file, encoding_mode)
    processed_content = file_manager.read_file(processed_file, encoding_mode)
    file_data = {
        "file_name": file_name,
        "file_size": file_size_bytes,
        "last_modification_date": last_modification_date,
        "raw_content": raw_content,
        "processed_content": processed_content,
    }
    data.append(file_data)

json_converter = JSONConverter(logger)
json_converter.serialize(data, "project_root/output/processed_data.json")

# Задание 3
file_manager.make_zip_archive("project_root/data", "project_root/backups")
backups = file_manager.get_file_paths_at_dir("project_root/backups", "zip")
zip_file_path = backups[-1]  # Берём самый свежий бэкап
file_manager.unzip_archive(zip_file_path, "project_root/restored")

# Задание 4
data = []
for file, processed_file in zip(files, processed_files):
    file_name = os.path.basename(processed_file)
    file_size_bytes = os.path.getsize(processed_file)
    encoding_mode = file_manager.read_file_encoding(file)
    raw_content = file_manager.read_file(file, encoding_mode)
    processed_content = file_manager.read_file(processed_file, encoding_mode)
    creation_date = datetime.fromtimestamp(
        os.path.getctime(processed_file), tz=timezone.utc
    )
    last_modification_date = datetime.fromtimestamp(
        os.path.getmtime(processed_file), tz=timezone.utc
    )
    file_data = {
        "file_name": file_name,
        "path": processed_file,
        "file_size": file_size_bytes,
        "creation_date": creation_date,
        "last_modification_date": last_modification_date,
    }
    data.append(file_data)

file_info_list = list(
    map(
        lambda entry: FileInfo(
            entry["file_name"],
            entry["path"],
            entry["file_size"],
            entry["creation_date"],
            entry["last_modification_date"],
        ),
        data,
    )
)
json_file_info_path = "project_root/output/file_info.json"
json_converter.custom_serialize(file_info_list, FileInfoEncoder, json_file_info_path)
restored_file_info_list = json_converter.custom_deserialize(
    json_file_info_path, FileInfoDecoder.decode
)
print(*restored_file_info_list, sep="\n\n")

file_info_json_schema_validator = FileInfoJSONSchemaValidator(logger)
file_info_dict_repr_generator = (file.dict_representation() for file in file_info_list)

for item in file_info_dict_repr_generator:
    file_info_json_schema_validator.isValid(item)
