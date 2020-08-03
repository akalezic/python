"""
File: temp_converter.py
-----------------------
This program asks the user what temperature conversion they would like to do,
asks them for the temperature they would like to convert from one measure to
the other, then prints the converted temperature.
"""

def main():
    # asks the user what conversion they would like to do
    conv = int(input("Would you like to do conversion 1 or 2? \n "
                     "1. Fahrenheit to Celsius\n 2. Celsius to Fahrenheit\n Enter 1 or 2: "))
    # based on user response asks for user to input a temperature in fahrenheit
    if conv == 1:
        fahr_in = float(input("Enter temperature in Fahrenheit: "))
        # converts temperature in fahrenheit to celsius
        cels_out = (fahr_in - 32) * 5/9
        # prints the original input in fahrenheit and the converted temp in celsius
        print("Temperature: " + str(fahr_in) + " C = " + str(cels_out) + "C")
    # based on user response asks for user to input a temperature in fahrenheit
    if conv == 2:
        cels_in = float(input("Enter temperature in Celsius: "))
        # converts temperature from celsius to fahrenheit
        fahr_out = (cels_in * 9/5) + 32
        # prints the original input in celsius and the converted temp in fahrenheit
        print("Temperature:" + str(cels_in) + " C = " + str(fahr_out) + " F")


if __name__ == '__main__':
    main()
