"""
File: hailstones.py
-------------------
** The description of this program is summarized/paraphrased from the assignment provided
in Stanford's Code in Place class offered in 2020 **
This is a file for the optional Hailstones problem, if
you'd like to try solving it.
The hailstones problem takes whatever number is input by the user and divides
even numbers by 2, and multiplies resulting odd numbers by 3 and adds 1 until
the final number is 1. The program then prints how many steps it took to reach 1.
"""


def main():
    #Takes in what number the user wants to run the hailstones process on
    num = int(input("Enter a number: "))
    # starts hailstone process count at 0 steps
    i = 0
    # makes sure that the process repeats while the resulting number is
    # greater than 1
    while num > 1:
        # if the number is even (ie remainder when divided by 2 is 0
        # divides the number by two and prints the resulting number
        if num % 2 == 0:
            even = num // 2
            print(str(num)+ " is even so I take half: "+ str(even) +".")
            # redefines num as even so that the process will repeat
            num = even
            # adds step to the step counter
            i = i + 1
        # if the number is odd multiplies by 3 and adds 1
        else:
            odd = (3 * num)+1
            # prints the initial number and the altered number
            # after multiplying by 3 and adding 1
            print(str(num)+ " is odd so I make 3n+1: "+str(odd)+ ".")
            # redefines num as odd so that the process repeats with the
            # new number after multiplying and adding
            num = odd
            # adds step to step counter
            i = i + 1
    # once the process ends the loop ends and this phrase prints how many
    # steps it took to reach 1
    print("The process took "+ str(i)+ " steps to reach 1.")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
