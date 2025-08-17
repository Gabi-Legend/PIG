import random
import time

def game() :
    player1Score = 0
    player2Score = 0
    print("First player turn")
    player1Rolls = int(input("How many times do you want to roll the dice? : "))

    if player1Rolls < 1:
        player1Rolls = int(input("Choose a value bigger than 0 : "))

    while player1Rolls != 0:
        dice = random.randint(1,6)
        if dice == 1:
            print(f"The dice rolled 1, the score is now 0")
            player1Score = 0
            break
        else:
            player1Score += dice
            print(f"You rolled {dice}, you score is now : {player1Score}")
        player1Rolls-=1
        if player1Rolls != 1:
            time.sleep(0.5)

    print("Second player turn")
    player2Rolls = int(input("How many times do you want to roll the dice? : "))

    if player2Rolls < 1:
        player2Rolls = int(input("Choose a value bigger than 0 : "))

    while player2Rolls != 0:
        dice = random.randint(1,6)
        if dice == 1:
            print(f"The dice rolled 1, the score is now 0")
            player2Score = 0
            break
        else:
            player2Score += dice
            print(f"You rolled {dice}, you score is now : {player2Score}")
        player2Rolls-=1
        if player2Rolls != 1:
            time.sleep(0.5)

    if player1Score == player2Score:
        print("It's a tie!")
    elif player2Score > player1Score:
        print("Player 2 won")
    else:
        print("Player 1 won")

while True:
    game()
    playAgain = input("Do you want to play again?(Y/N): ").lower()
    if playAgain in ["n","no","nope","na"]:
        break