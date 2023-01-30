from typing import Callable

intro_fn = Callable[[str, str, int], None]


class Person:
    def __init__(self, first_name: str, last_name: str, age: int, introduction: intro_fn):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        introduction(self.first_name, self.last_name, self.age)
