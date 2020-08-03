"""
File: nimm.py
-------------
** The description of this program is summarized/paraphrased from the assignment provided
in Stanford's Code in Place class offered in 2020 **
This mimics the game of Nimm, which starts with 20 stones. 2 players must take turns and can
remove either one or two stones from the pile when its their turn. They continue playing until
there are no stones left. The last person to take a stone loses.
"""

stones = 20


def main():
    # provides starting number of 20 stones
    stones = 20
    # starts with player 1
    player = 1
    while stones > 0:
        print("There are " + str(stones) + " stones left")
        # asks for user input about how many stones they would like to remove
        remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
        # if the user inputs a number that is other than 1 or 2 invalid option message
        # prints and asks for another input
        while remove > 2 or remove < 1:
            remove = int(input("Please enter 1 or 2: "))
        stones = stones - remove
        print("")
        # alternates players between rounds
        if player == 1:
            player = player + 1
        else:
            player = player - 1

    else:
        # announces winning player
        print("Player "+str(player)+ " wins!")


if __name__ == '__main__':
    main()