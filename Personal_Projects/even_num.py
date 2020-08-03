"""
File: even_num.py
-----------------
Prints the first 100 even numbers backwards.
"""

def main():
# prints first 100 even numbers backwards
for i in range(200):
    var = (200 - i)
    if var % 2 == 0:
        print(var)

if __name__ == '__main__':
    main()