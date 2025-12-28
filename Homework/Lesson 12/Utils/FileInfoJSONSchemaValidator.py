from Utils.Logger import Logger
from jsonschema import validate, ValidationError, FormatChecker


class FileInfoJSONSchemaValidator:
    __json_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "path": {"type": "string"},
            "size": {"type": "integer", "minimum": 0},
            "creation_date": {"type": "string", "format": "date-time"},
            "last_modification_date": {"type": "string", "format": "date-time"},
        },
        "required": ["name", "path", "size", "creation_date", "last_modification_date"],
    }

    def __init__(self, logger: Logger):
        self.__logger = logger

    def isValid(self, document: object):
        """
        Валидирует JSON объект document, используя JSON схему для класса FileInfo
        Args:
            document (object): Словарное представление класса FileInfo
        """
        try:
            validate(
                instance=document,
                schema=self.__json_schema,
                format_checker=FormatChecker(),
            )
            self.__logger.log(f"{document} валиден")
        except ValidationError as error:
            self.__logger.log(f"{document} невалиден: {error}")
