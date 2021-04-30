#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: April 2021
# This program checks if a person chose the right number between 0 and 9

import constants


def main():
    # This function checks if the person chose right or wrong number

    # Input

    correct_number = int(input("Enter the number between 0 and 9: "))
    print("")

    # process
    if correct_number > constants.SECRET_NUMBER:
        # Output
        print("Too high!")

    if correct_number < constants.SECRET_NUMBER:
        # Output
        print("Too low!")

    if correct_number == constants.SECRET_NUMBER:
        # Output
        print("Correct!")


if __name__ == "__main__":
    main()
