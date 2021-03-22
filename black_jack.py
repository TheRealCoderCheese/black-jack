import random

listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

username = input("enter you username: ")

score, computer_score = 0, 0


class Player:
    def __init__(self, score,computer_score):
        pass

    def main(self):
        score = random.choice(listOfNumbers)
        computer_score = random.choice(listOfNumbers)
        print(f"player 1 this is your deck: {score}")
        print(f"this is the computers score: {computer_score}")

    def turn(self):
        turn = input("do you want to hit, stand or end(h,s,e)")
        if turn == "hit" or "h":
            score += random.choice(listOfNumbers)
            print(score)
        elif turn == "stand" or "s":
            score += 0
        elif turn == "end" or "e":
            print("succesfully ended game")

    def check_if_game_end(self):
        if score == 21 and computer_score < 21:
            print(f"{username} wins")
        elif score == 21 and computer_score > 21:
            print(f"{username} wins")
        elif score > 21:
            print("the computer won")
        elif computer_score == 21 and score < 21:
            print("the computer won")


p = Player(score, computer_score)

p.main()

for i in range(6):
    p.turn()
    p.check_if_game_end()
