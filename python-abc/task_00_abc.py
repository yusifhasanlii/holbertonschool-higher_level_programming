#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class representing an Animal.
    Inherits from ABC to enforce abstract behavior.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        It does not have a body here.
        """
        pass


class Dog(Animal):
    """
    Subclass representing a Dog.
    Inherits from Animal.
    """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """
    Subclass representing a Cat.
    Inherits from Animal.
    """
    def sound(self):
        return "Meow"
