"""File to define Fish class."""

__author__ = "730748337"


class Fish:
    age: int

    def __init__(self):
        """Initialize a new Fish."""
        self.age = 0

    def one_day(self):
        """Increase age by 1 each day."""
        self.age += 1
