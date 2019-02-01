from random import randint

t = ["rock","paper","scissor"]

computer = t[randint(0,2)]
player = True

while player == True:
    player = input("Enter your choice:")

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!",computer,"covers",player,".")
        else:
            print("You win!",player,"smashes",computer,".")

    elif player == "scissor":
        if computer == "rock":
            print("You lose!",computer,"smashes",player,".")
        else:
            print("You win!",player,"cuts",computer,".")

    elif player == "paper":
        if computer == "rock":
            print("You win!",player,"covers",computer,".")
        else:
            print("You lose!",computer,"cuts",player,".")

    else:
        print("That is not a valid play.Check your spelling.")

    player = True
    computer = t[randint(0,2)]