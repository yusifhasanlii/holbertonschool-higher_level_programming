#!/usr/bin/python3
"""
This module demonstrates the use of Mixins in Python.
It defines SwimMixin, FlyMixin, and a Dragon class that uses both.
"""


class SwimMixin:
    """Mixin that adds swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from SwimMixin and FlyMixin.
    This demonstrates composing behavior from multiple mixins.
    """

    def roar(self):
        """Prints a roaring message specific to the dragon."""
        print("The dragon roars!")
