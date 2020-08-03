"""
File: subtract_numbers.py
-------------------------
** The description of this program is summarized/paraphrased from the assignment provided
in Stanford's Code in Place class offered in 2020 **
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    ## prints This program subtracts one number from another. in the terminal
    print("This program subtracts one number from another.")
    ## allows user to enter an input in the terminal, which is then converted
    # to a float and saved as the variable num1
    num1 = float(input("Enter first number: "))
    ## allows user to enter an input, which is then converted to a float
    ## and saved as the variable num2
    num2 = float(input("Enter second number: "))
    ## subtracts num2 from num1 and saves that value as variable total
    total = num1 - num2
    ## prints This result is total in the terminal after converting total
    ## from a float to a string
    print("The result is "+str(total)+"")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
