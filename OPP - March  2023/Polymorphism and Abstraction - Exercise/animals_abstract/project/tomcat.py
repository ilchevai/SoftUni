from abc import ABC, abstractmethod

from project.cat import Cat


class Tomcat(Cat, ABC):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def make_sound(self):
        return "Hiss"
