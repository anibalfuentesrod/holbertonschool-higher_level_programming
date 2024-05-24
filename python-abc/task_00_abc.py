#!/usr/bin/env python3
from abc import ABC, abstractmethod

"""
Class name Animal thas has two subclasess
"""


class Animal(ABC):
    """
    Abstract base class name Animal

    Methods:
        sound()
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method tha sould be implemented by subclass
        """
        pass


class Dog(Animal):
    """
    Dog class, a subclass of Animal

    Methods:
        sound(Bark)
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Cat class, subclass of Animal

    Methods:
        sound(Meow)
    """
    def sound(self):
        return "Meow"
