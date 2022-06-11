"""This module simulates rock, paper and scissors game."""

import random


CHOICES = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
CHOICES_LIST = ['R', 'P', 'S']

def play_game(user_choice, computer_choice):
    """Compares user choice and that of computer and checks winner"""
    print(f'Player ({user_choice}) : CPU ({computer_choice})')
    if user_choice == computer_choice:
        print("It's a tie. Please try again...")
        return 0
    elif user_choice == 'Rock':
        if computer_choice == 'Scissors':
            print("Hurray! You won. 'Rock' breaks 'Scissors'")
            scores['user'] = scores['user'] + 1 # Update scores
            return 1
        else:
            print("Computer won. 'Paper' covers 'Rock'")
            scores['computer'] = scores['computer'] + 1 # Update scores
            return 2
    elif user_choice == 'Paper':
        if computer_choice == 'Rock':
            print("Hurray! You won. 'Paper' covers 'Rock'")
            scores['user'] = scores['user'] + 1 # Update scores
            return 1
        else:
            print("Computer won. 'Scissors' cuts 'Paper'")
            scores['computer'] = scores['computer'] + 1 # Update scores
            return 2
    elif user_choice == 'Scissors':
        if computer_choice == 'Paper':
            print("Hurray! You won. 'Scissors' cuts 'Paper'")
            scores['user'] = scores['user'] + 1 # Update scores
            return 1
        else:
            print("Computer won. 'Rock' breaks 'Scissors'")
            scores['computer'] = scores['computer'] + 1 # Update scores
            return 2


scores = {'user': 0, 'computer': 0}
print("\n\nSCORES:")
print(f"| You: {scores['user']} | ------ | CPU: {scores['computer']} |\n")
game_on = True
while game_on:
    print("CHOICES = 'R: Rock', 'P: Paper' and 'S: Scissors'. (Q: Quit)")
    user_choice = input("Make a choice: ")
    if user_choice.upper() == 'Q':
        print("Thank you for playing Rock, Paper, Scissors game. \n Built by \
Festus Ali")
        game_on = False
    elif user_choice.upper() not in CHOICES:
        print('Incorrect option. Please choose from presented choices')
        continue
    else:
        user_choice = CHOICES[user_choice.upper()]
        # random.choice cannot pick from dictionary. Use CHOICE_LIST to subset
        computer_choice = CHOICES[random.choice(CHOICES_LIST)]
        result = play_game(user_choice, computer_choice)
        print("\n\nCURRENT SCORES:")
        print(f"| You: {scores['user']} | ------ | CPU: \
            {scores['computer']} |\n")
