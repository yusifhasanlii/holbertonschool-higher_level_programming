#!/usr/bin/python3
"""
This module defines an abstract class Shape and concrete classes
Circle and Rectangle. It also includes a function shape_info
to demonstrate duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    Enforces implementation of area and perimeter.
    """

    @abstractmethod
    def area(self):
        """Abstract method for area calculation"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter calculation"""
        pass


class Circle(Shape):
    """
    Class representing a Circle.
    Inherits from Shape.
    """
    def __init__(self, radius):
        """Initialize Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a Rectangle.
    Inherits from Shape.
    """
    def __init__(self, width, height):
        """Initialize Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of the object passed.
    Relies on duck typing: assumes the object has area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
