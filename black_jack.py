import random

listOfNumbers = [1,2,3,4,5,6,7,8,9,10,11]

username = input("enter you username: ")

score = 0
computer_score = 0
def main():
    global score, computer_score
    score = random.choice(listOfNumbers)
    computer_score = random.choice(listOfNumbers)
    print(f"player 1 this is your deck {score}")
    print(f"this is the computer's deck {computer_score}")

def turn():
    global score
    turn = input("do you want to hit, stand or end(h,s,e)")
    if turn == "hit" or "h":
        score += random.choice(listOfNumbers)  
        print(score)
    elif turn == "stand" or "s":
        score += 0
    elif turn == "end" or "e":
        print("succesfully ended game")

def computer_turn():
    global score, computer_score
    if score == 20 and computer_score < 20:
        computer_score += random.choice(listOfNumbers)
    elif score >=10 and computer_score == 20:
        computer_score += 0
    elif score <15 and computer_score >10:
        computer_score += random.choice(listOfNumbers)

def check_if_game_end():
    global score, computer_score
    if score == 21 and computer_score <21:
        print(f"{username} wins")
    elif score == 21 and computer_score >21:
        print(f"{username} wins")
    elif score > 21:
        print("the computer won")
    elif computer_score == 21 and score <21:
        print("the computer won")
main()
#hello



