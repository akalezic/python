"""
File: num_guessing.py
---------------------
This program acts as a number guessing game that provides the user with hints about
whether their guess is too high, too low, or outside of the interval. A new number
guessing game begins once the user has guessed correctly.
"""

import random

# can change minimum and maximum value of interval without having to locate it each time in the code
# and change it
MIN = 0
MAX = 100

def main():
    print("Hello! Let's play a number guessing game. Press ctrl-c to quit.")
    # asks player for name
    name = str(input("Please enter your name: "))
    # chooses a random integer within a range
    rand = random.randint(MIN,MAX)
    print(name +" I am thinking of an integer on the interval [" + str(MIN) + "," + str(MAX) + "].")
    # takes guess from user
    guess = int(input("Please enter your guess: "))
    # will keep asking for guesses while the guess is not equal to the random integer
    while guess != rand:
        # if the guess is too high notifies the user of that and asks for a new guess
        if guess > rand:
            print(name + ", your guess was too high!\n")
            guess = int(input("Please enter your guess: "))
        # if the guess is too low notifies the user of that and asks for a new guess
        if guess < rand:
            print(name + ", your guess was too low!\n")
            guess = int(input("Please enter your guess: "))
        # if the guess is outside of the range notifies the user and asks for a new guess
        if guess > MAX or guess < MIN:
            print(name + " your guess is outside of the range of values.")
            guess = int(input("Please enter your guess: "))
        # if the guess is correct then the user is congratulated and a new game starts
        if guess == rand:
            print("Congratulations " + name + " you got it!\n")
            print(name +" I am thinking of an integer on the interval [" + str(MIN) + "," + str(MAX) + "].")
            guess = int(input("Please enter your guess: "))


if __name__ == '__main__':
    main()