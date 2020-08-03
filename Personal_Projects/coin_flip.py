"""
File: coin_flip.py
------------------
This program acts as a coin-flipper, where a random number is generated. If the
random number that is generated is even then the outcome will be heads, whereas
if it's odd, the outcome of the coin flip will be tails.
"""

import random

def main():
# Asks the user if they would like to flip a coin
    response = str(input("Would you like to flip a coin? Enter Yes or No: "))
# while the response is yes the program generates a random number, so the progra
# will loop, providing "coin flips" until the user says no
    while response == str("Yes") or response == ("yes"):
        num = random.randint(0,1000)
        # if the random number is even the outcome printed is heads, then asks
        # if the user would like to flip a coin again, and generates a new random
        # number
        if num % 2 == 0:
            print("Heads")
            response = input("Would you like to flip a coin? Enter Yes or No: ")
            num = random.randint(0, 1000)
        # if the random number is odd the outcome printed is tails, then it asks
        # if the user would like to flip a coin again, and generates a new random
        # number
        else:
            print("Tails")
            response = input("Would you like to flip a coin? Enter Yes or No: ")
            num = random.randint(0, 1000)
    # if the user response is no (or No if the person reads the prompt literally
    # then the program prints "Okay see you next time!" and ends
    if response == ("No") or response == ("no"):
        print("Okay, see you next time!")


if __name__ == '__main__':
    main()