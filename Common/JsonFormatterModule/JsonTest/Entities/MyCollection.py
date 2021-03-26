from typing import TypeVar, Generic, List, Dict

from Common.JsonFormatterModule.JsonContract import JsonContract

T = TypeVar("T")


class MyCollection(Generic[T], JsonContract):
    inner_list: List[T]
    inner_dict: Dict[int, T]

    def __init__(self, items: List[T] = None):
        super().__init__({
            "l": "inner_list",
            "d": "inner_dict"
        })

        if items is not None:
            self.inner_list = items
            self.inner_dict = dict(((index, item) for index, item in enumerate(items)))

    def __eq__(self, other):
        if self.inner_list is other.inner_list or self.inner_dict is other.inner_dict:
            return False
        if len(self.inner_list) != len(other.inner_list) or \
                len(self.inner_dict.keys()) != len(other.inner_dict.keys()):
            return False
        for index, item in enumerate(self.inner_list):
            if item != other.inner_list[index]:
                return False

        for k, v in self.inner_dict.items():
            if self.inner_dict[k] != other.inner_dict[k]:
                return False
        return True
