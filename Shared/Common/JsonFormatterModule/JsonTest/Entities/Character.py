from Shared.Common.JsonFormatterModule.JsonContract import JsonContract


class Character(JsonContract):
    age: int
    salary: int

    def __init__(self, age: int = None, salary: int = None):
        super().__init__({
            "a": "age",
            "n": "salary"
        })

        if age is not None:
            self.age = age
        if salary is not None:
            self.salary = salary

    def __eq__(self, other):
        return self.age == other.age and self.salary == other.salary
