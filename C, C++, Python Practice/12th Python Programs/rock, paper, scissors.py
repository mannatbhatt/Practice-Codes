import random

options = ('rock', 'paper','scissors')
running = True #putting True directly the loop won't be able to find the break statement, that's why we put a boolean variable

while running:

    player = None
    computer = random.choice(options)         #Reset the player and new random choice

    while player not in options:
        player=input("Enter a choice (rock, paper or scissors) : ")

    print(f"Player : {player}") 
    print(f"Computer :{computer}")

    if player == computer:
        print("It's a tie")
    elif player == 'rock' and computer == 'scissors':
        print("You win!")
    elif player == 'paper' and computer == 'rock' :
        print("You win!")
    elif player == 'scissors' and computer == 'paper' :
        print("You win!")
    else:
        print("You lose :( ")

    play_again=input("Do you wanna play again? (y/n) :")

    if play_again != "y":
        running = False

print("Thanks for playing!")
