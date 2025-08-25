import random


class Player:
    def __init__(self, name=None, choice=None, score=None):
        self.name = name
        self._choice = choice
        self.score = 0

    @classmethod
    def cpu_make_choice(cls):
        options = ["Rock", "Paper", "Scissors"]
        choice = random.choice(options)
        return choice

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, value):
        if value in ["Rock", "Paper", "Scissors"]:
            self._choice = value

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        elif self.choice == other.choice:
            return True

    def __gt__(self, other):
        if not isinstance(other, Player):
            return False
        if self.choice == "Rock" and other.choice == "Scissors":
            return True
        if self.choice == "Paper" and other.choice == "Rock":
            return True
        if self.choice == "Scissors" and other.choice == "Paper":
            return True
        return False
