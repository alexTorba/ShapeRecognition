from abc import ABC, abstractmethod

from typing import List

from Shared.Common.JsonFormatterModule.JsonContract import JsonContract
from Shared.Common.JsonFormatterModule.JsonTest.Entities.Character import Character


class BaseClass(ABC):
    @abstractmethod
    def method(self):
        pass


class DerivedClass(BaseClass, JsonContract):
    field1: str
    field2: int
    characters: List[Character]

    def __init__(self, field1: str = None,
                 field2: int = None,
                 characters: List[Character] = None):
        super().__init__({
            "f1": "field1",
            "f2": "field2",
            "c": "characters",
            "d": "derived_class"
        })

        if field1 is not None:
            self.field1 = field1
        if field2 is not None:
            self.field2 = field2
        if characters is not None:
            self.characters = characters

    def method(self):
        print("derived class")

    def __eq__(self, other):
        if self.field1 is other.field1 or self.characters is other.characters:
            return False

        for index, item in enumerate(self.characters):
            if item != other.characters[index]:
                return False
        return self.field1 == other.field1 and self.field2 == other.field2

    @staticmethod
    def build() -> "DerivedClass":
        characters = [Character(age=13, salary=400), Character(age=18, salary=500), Character(age=20, salary=1000)]
        return DerivedClass("text", 123, characters)
