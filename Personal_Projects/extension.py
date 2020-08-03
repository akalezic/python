"""
File: extension.py
------------------
Prints multiples of 3 under 1000.
"""

def main():
    # prints multiples of 3 under 1000
    for i in range(1000):
        if i % 3 == 0:
            print(i)


if __name__ == '__main__':
    main()
