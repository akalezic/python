"""
File: moon_weight.py
--------------------
This program takes in the user's input of a weight amount and returns what the
equivalent weight would be on the moon.
"""


def main():
    weight_on_earth = int(input("Enter a weight on Earth:"))
    weight_on_moon = .165 * weight_on_earth
    print("Equivalent weight on moon:" + str(weight_on_moon) + ".")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
