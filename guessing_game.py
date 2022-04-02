#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: April 2022
# This program lets the user guess a number between 0 and 9

import random


def main():
    # this function lets the user guess a number between 0 and 9

    guess_variable = random.randint(0, 9)  # a number between 0 and 9

    # input
    try:
        number_guessed = int(input("Enter a number between 0 and 9: "))

        # process & output

        if number_guessed == guess_variable:
            print("You guessed correct!")

        else:
            print("You guessed wrong!")
            print("The number was {}.".format(guess_variable))
    except Exception:
        print("This was not an integer")
    finally:
        print("")
        print("Done")


if __name__ == "__main__":
    main()
