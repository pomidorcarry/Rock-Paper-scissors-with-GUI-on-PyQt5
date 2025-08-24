
class Game:

    @classmethod
    def game_result(cls,player,cpu):
        if not (player.choice and cpu.choice):
            print("Error\nnot enough choices provided")
        elif player == cpu:
            return "It's a draw!"
        elif player > cpu:
            player.score += 1 
            return "You won!"
        else:
            player.score -= 1
            return "You've lost!"
        