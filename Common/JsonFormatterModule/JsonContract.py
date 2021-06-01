from abc import ABC, abstractmethod
from copy import copy
from typing import Dict


# noinspection PyDeepBugsSwappedArgs


class JsonContract(ABC):
    """Each class that will override this class must have :\n
    - annotations for all fields\n
    - implement _json_field\n
    - open ctor\n"""

    __json_fields: Dict[str, str]  # key = minimized field name, value = full field name

    __field_json: Dict[str, str] = NotImplemented  # key = full field name, value = minimized field name

    @abstractmethod
    def __init__(self, json_fields: Dict[str, str]):
        self.__json_fields = json_fields

    def _update_json_fields(self, json_fields: Dict[str, str]) -> None:
        self.__json_fields.update(json_fields)

    def to_minimize_dict(self) -> dict:
        """format object to minimize dict"""
        if self.__field_json is NotImplemented:
            self.__field_json = dict(zip(self.__json_fields.values(), self.__json_fields.keys()))
        for n, v in self.__dict__.items():
            if not n.startswith("_") and n in self.__field_json:
                yield self.__field_json[n], copy(v)

    def json_to_field(self, min_field: str) -> str:
        """convert minimize field to full name field"""
        return self.__json_fields.get(min_field)

    def to_json_str(self) -> str:
        from Common.JsonFormatterModule.JsonFormatter import JsonFormatter  # to avoid cycle dependencies
        return JsonFormatter.serialize(self)
