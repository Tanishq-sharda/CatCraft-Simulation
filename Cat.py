"""
Tanishq Sharda
400588854
Engineering 1
ENG 1P13
Sam Scott
Fall 2024

This program contains the Cat class for the CatCraft game.
"""

import random


class Cat:
    """
    A class to represent a Cat in the CatCraft game.
    """

    def __init__(self, name):
        """
        Initializes a new Cat object with default values.

        Parameters:
        name (str): The name of the cat.
        """
        self._name = name
        self._fish = 0
        self._tame = False
        self._alive = True
        self._health = 2.0

    def get_name(self):
        """
        Returns the cat's name.

        Returns:
        str: The cat's name.
        """
        return self._name

    def feed(self, fish):
        """
        Feeds the cat a chosen number of fish.

        Health increases by 1 per fish up to a maximum of 4.
        The cat has a 50% chance of becoming tame for each fish fed.
        If the cat has more than 3 fish in its stomach, it dies.

        Parameters:
        fish (int): Number of fish to feed.

        Raises:
        ValueError: If the cat is dead or if fish is negative.
        """
        if not self._alive:
            raise ValueError(f"{self._name} is already dead. You can't feed a dead cat.")

        if fish < 0:
            raise ValueError("You cannot give a negative number of fish.")

        for _ in range(fish):
            self._fish += 1

            if self._fish > 3:
                self._alive = False
                self._health = 0.0
                return

            self._health = min(4.0, self._health + 1.0)

            if random.random() < 0.5:
                self._tame = True

    def hit(self):
        """
        Hits the cat, reducing its health by 1.5 and making it wild.

        Raises:
        ValueError: If the cat is already dead.
        """
        if not self._alive:
            raise ValueError(f"{self._name} is already dead. You can't hit a dead cat.")

        self._tame = False
        self._health = max(0.0, self._health - 1.5)

        if self._health == 0.0:
            self._alive = False

    def night(self):
        """
        Simulates the end of a night.

        If the cat is alive, one fish is removed from its stomach.
        If the cat is tame and had fish, it leaves a gift.
        If the fish count becomes 0, the cat becomes wild.

        Returns:
        bool: True if the cat leaves a gift, False otherwise.
        """
        if not self._alive:
            return False

        had_fish = self._fish > 0
        gave_gift = self._tame and had_fish

        self._fish = max(0, self._fish - 1)

        if self._fish == 0:
            self._tame = False

        return gave_gift

    def __str__(self):
        """
        Returns a string representation of the cat.

        Returns:
        str: Summary of the cat's status.
        """
        life = "DEAD" if not self._alive else ""
        cat_type = "Tame" if self._tame else "Wild"

        if life:
            return f"{life} {cat_type} Cat {self._name}: {self._health:.1f} health, {self._fish} fish"
        return f"{cat_type} Cat {self._name}: {self._health:.1f} health, {self._fish} fish"
    
    