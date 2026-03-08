#!/usr/bin/python3
"""
This module explores multiple inheritance with Fish, Bird, and FlyingFish.
It demonstrates how methods are overridden and resolved.
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Standard swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Standard flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    FlyingFish inherits from both Fish and Bird.
    Demonstrates overriding methods from multiple parents.
    """

    def fly(self):
        """Overrides Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides habitat method from both Fish and Bird."""
        print("The flying fish lives both in water and the sky!")
