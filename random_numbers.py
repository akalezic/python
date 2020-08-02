"""
File: random_numbers.py
-----------------------
** The description of this program is summarized/paraphrased from the assignment provided
in Stanford's Code in Place class offered in 2020 **
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive using the random library.
"""

import random

## defines min_random as 0
MIN_RANDOM = 0
## defines max_random as 100
MAX_RANDOM = 100
## defines num_random as 10
NUM_RANDOM = 10

def main():
    ## prints 10 random integers between min_random (0) and max_random (100)
    for i in range(NUM_RANDOM):
        print(random.randint(MIN_RANDOM,MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
