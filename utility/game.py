import random

class Game:
    @classmethod
    def cpu_make_choice(cls):
        options = ["Rock","Paper","Scissors"]
        choice = random.choice(options)
        return choice
    @classmethod
    def game_result(cls,player,cpu):
        if player.choice and cpu.choice:
            player.score += 1 
            return "You won!"
        