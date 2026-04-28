"""File to define Bear class."""

__author__ = "730748337"


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a new Bear."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increase age by 1 and decrease hunger_score by 1 each day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Update the bear's hunger score after eating fish."""
        self.hunger_score += num_fish
