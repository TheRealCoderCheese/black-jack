import random

listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


score, computer_score = 0, 0

username = input("enter in your username: ")

turn = 0

computer_move = 0


class Player:
    def __init__(self, score, computer_score, username, turns, computer_move):
        self.score = score
        self.computer_score = computer_score
        self.username = username
        self.turns = turns
        self.computer_move = computer_move

    def main(self):
        self.score += random.choice(listOfNumbers)
        self.computer_score += random.choice(listOfNumbers)
        print(f"player 1 this is your deck: {self.score}")
        print(f"this is the computers score: {self.computer_score}")

    def turn(self):
        turn = input("do you want to hit, stand or end(h,s,e)")
        if turn == "hit" or "h":
            self.turns += 1
            self.score += random.choice(listOfNumbers)
            print(self.score)
        elif turn == "stand" or "s":
            self.turns
            self.score += 1
        elif turn == "end" or "e":
            print("succesfully ended game")

    def computer_turn(self):
        if self.score == 20 and self.computer_score < 15:
            self.computer_score += random.choice(listOfNumbers)
            self.computer_move += 1
        elif self.computer_score == 20:
            self.computer_score += 0
            self.computer_move += 1
        elif self.computer_score < 15 and self.score > 15:
            self.computer_score += random.choice(listOfNumbers)
            self.computer_move += 1
        else:
            self.computer_score += random.choice(listOfNumbers)
            self.computer_move += 1

    def check_if_game_end(self):
        if self.score == 21 and computer_score < 21:
            print(f"{self.username} wins")
            return "game-over"
        elif self.computer_score == 21 and self.score < 21:
            print("the computer won")
            print(f"this is the computers score: {self.computer_score}")
            return "game-over"
        elif self.turns == 5 and self.score < 21 and self.computer_score != 21:
            print(f"{self.username} wins")
            return "game-over"
        elif self.computer_move == 5 and self.computer_score < 21 and self.score != 21:
            print("the computer won")
            print(f"this is the computers score: {self.computer_score}")
            return "game-over"
        elif self.score > 21 and self.computer_score <= 21:
            print("the computer won")
            print(f"this is the computers score: {self.computer_score}")
            return "game-over"
        elif self.computer_score > 21 and self.score <= 21:
            print(f"{self.username} wins")
            return "game-over"

p = Player(score, computer_score, username, turn, computer_move)

p.main()

while True:
    if p.check_if_game_end() == "game-over":
        break
    else:
        p.turn()
        p.check_if_game_end()
        p.computer_turn()
        p.check_if_game_end()
