"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730748337"


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish > 3 years old and Bears > 5 years old."""
        self.fish = [f for f in self.fish if f.age <= 3]
        self.bears = [b for b in self.bears if b.age <= 5]

    def remove_fish(self, amount: int):
        """Removes the frontmost 'amount' of Fish from the river."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)

    def bears_eating(self):
        """Simulate bears eating if there are enough fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Remove Bears with a hunger score less than 0."""
        self.bears = [b for b in self.bears if b.hunger_score >= 0]

    def repopulate_fish(self):
        """Simulate Fish reproduction."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Simulate Bear reproduction."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def __str__(self) -> str:
        """String representation of the River status."""
        return f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}"

    def __add__(self, other_riv: River) -> River:
        """Combine two rivers to create a larger one."""
        total_fish = len(self.fish) + len(other_riv.fish)
        total_bears = len(self.bears) + len(other_riv.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> River:
        """Multiply the population of the river by a factor."""
        total_fish = len(self.fish) * factor
        total_bears = len(self.bears) * factor
        return River(total_fish, total_bears)

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Simulate one week (7 days) in the river."""
        for _ in range(7):
            self.one_river_day()
