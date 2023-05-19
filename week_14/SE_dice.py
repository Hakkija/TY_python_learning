import random


class Dice:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def throw(self):
        return random.randint(1, 6)

    def __str__(self):
        return f"Dice {self.name}, {self.wins} wins"


class FalseDice(Dice):
    def throw(self):
        return random.choices([1, 2, 3, 4, 5, 6], weights=[1, 1, 1, 1, 1, 2])[0]

    def __str__(self):
        return f"False dice {self.name}, {self.wins} wins"


class Game:
    def __init__(self, dice1, dice2):
        self.dice1 = dice1
        self.dice2 = dice2

    def play(self):
        score1, score2 = 0, 0
        while score1 < 100 and score2 < 100:
            score1 += self.dice1.throw()
            score2 += self.dice2.throw()
        if score1 >= 100 and score2 < 100:
            self.dice1.wins += 1
        elif score2 >= 100 and score1 < 100:
            self.dice2.wins += 1


# Main program
dice_list = [Dice(f"Player{i}") for i in range(1, 9)]
dice_list.append(FalseDice("FalsePlayer1"))
dice_list.append(FalseDice("FalsePlayer2"))

for i in range(len(dice_list)):
    for j in range(i + 1, len(dice_list)):
        game = Game(dice_list[i], dice_list[j])
        game.play()

dice_list.sort(key=lambda d: -d.wins)
for dice in dice_list:
    print(dice)
