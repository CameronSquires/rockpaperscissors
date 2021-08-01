import random

actions = ["Rock", "Paper", "Scissors"]

def playGame():
    makeAction = input("Please pick rock, paper or scissors. ").upper()

    if makeAction == "R" or "ROCK":
        x = actions[0]
    elif makeAction == "P" or "PAPER":
        x = actions[1]
    elif makeAction == "S" or "SCISSORS":
        x = actions[2]


    computersChoice = random.choice(actions)

    if computersChoice == actions[0]:
        print(f"Computer picked: {computersChoice}")
        if x == actions[0]:
            print("This game was a draw.")
        if x == actions[1]:
            print("You win!")
        if x == actions[2]:
            print("You lose!")

    if computersChoice == actions[1]:
        print(f"Computer picked: {computersChoice}")
        if x == actions[0]:
            print("You lose!")
        if x == actions[1]:
            print("This game was a draw.")
        if x == actions[2]:
            print("You win!")

    if computersChoice == actions[2]:
        print(f"Computer picked: {computersChoice}")
        if x == actions[0]:
            print("You win!")
        if x == actions[1]:
            print("You lose!")
        if x == actions[2]:
            print("This game was a draw.")


playGame()