
#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: October 17th 2022
# This program will generate a number between
# 0 and 9 and have you guess what number it is
import random


def main():
    # generate random number between 0 and 9
    correct_answer = random.randint(0, 9)

    # Getting the random number
    print("Guess a number between 0 and 9")

    # asking user to guess a number between 0 and 9
    user_guess_as_string = input("What is your guess? ")

    try:
        # making the string into an Int
        user_guess_as_int = int(user_guess_as_string)

    except Exception:
        print(user_guess_as_string, "is not an integer")

    else:
        # Determining whether the answer is correct
        if user_guess_as_int == correct_answer:
            print(user_guess_as_int, " is correct! ")
        else:
            print(
                user_guess_as_int,
                " is not correct, the correct answer was",
                correct_answer,
            )

    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
