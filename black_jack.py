import random

listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


score = 0

computer_score = 0

username = input("enter in your username: ")

class Player:
    def __init__(self, score,computer_score, username):
        self.score = score
        self.computer_score = computer_score
        self.username = username

    def main(self):
        self.score += random.choice(listOfNumbers)
        self.computer_score += random.choice(listOfNumbers)
        print(f"player 1 this is your deck: {self.score}")
        print(f"this is the computers score: {self.computer_score}")

    def turn(self):
        turn = input("do you want to hit, stand or end(h,s,e)")
        if turn == "hit" or "h":
            self.score += random.choice(listOfNumbers)
            print(self.score)
        elif turn == "stand" or "s":
            self.score += 0
        elif turn == "end" or "e":
            print("succesfully ended game")

    def check_if_game_end(self):
        if self.score == 21 and computer_score < 21:
            print(f"{self.username} wins")
        elif self.score == 21 and self.computer_score > 21:
            print(f"{self.username} wins")
        elif self.score > 21:
            print("the computer won")
        elif self.computer_score == 21 and self.score < 21:
            print("the computer won")
    def computer_turn():
        if self.score == 20 and self.computer_score < 15:
            self.computer_score += random.choice(listOfNumbers)
        elif self.computer_score == 20:
            self.computer_score += 0
        elif self.computer_score <15 and score >15:
            self.computer_score += random.choice(listOfNumbers)



p = Player(score, computer_score, username)

p.main()

for i in range(6):
    p.turn()
    p.check_if_game_end()
    '''p.computer_turn()
    p.check_if_game_end()'''
