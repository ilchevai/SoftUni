from abc import ABC, abstractmethod

from project.cat import Cat


class Kitten(Cat, ABC):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return "Meow"
