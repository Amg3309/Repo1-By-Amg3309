# Stone Paper Scissors
# Hope you enjoy your game
import random

ComOptions = ['St', 'P', 'Sc']
ComChoice = random.choice(ComOptions)
print("Welcome to Stone, Paper and Scissors")
UserChoice = input("Enter St for Stone, P for Paper and Sc for Scissors\n")
UserChoice = UserChoice.lower()

if ComChoice == 'St' and UserChoice == 'st':
    print("You Entered Stone and the Computer Entered Stone.")
    print("It's a tie")
elif ComChoice == 'St' and UserChoice == 'p':
    print("You Entered Paper and the Computer Entered Stone.")
    print("You win")
elif ComChoice == 'St' and UserChoice == 'sc':
    print("You Entered Scissors and the Computer Entered Stone.")
    print("You Lose")
elif ComChoice == 'P' and UserChoice == 'p':
    print("You Entered Paper and the Computer Entered Paper.")
    print("It's a tie")
elif ComChoice == 'P' and UserChoice == 'st':
    print("You Entered Stone and the Computer Entered Paper.")
    print("You Lose")
elif ComChoice == 'P' and UserChoice == 'sc':
    print("You Entered Scissor and the Computer Entered Paper.")
    print("You Win")
elif ComChoice == 'Sc' and UserChoice == 'sc':
    print("You Entered Scissors and the Computer Entered Scissors.")
    print("It's a tie")
elif ComChoice == 'Sc' and UserChoice == 'st':
    print("You Entered Stone and the Computer Entered Scissors.")
    print("You Win")
elif ComChoice == 'Sc' and UserChoice == 'p':
    print("You Entered Paper and the Computer Entered Scissor.")
    print("You Lose")
else:
    print("Invalid Input")
