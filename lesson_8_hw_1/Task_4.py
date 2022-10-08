from random import *
from string import *


def main():
    print("The password was generated successfully:", generate_password())


def generate_password():
    digit_array = digits
    big_letter = ascii_uppercase
    small_letter = ascii_lowercase
    under_score = "_"
    result_password = choices(digit_array) + choices(small_letter) + choices(big_letter)
    for i in range(1, 6):
        result_password += choices(big_letter + small_letter + under_score)
        while result_password[i] == result_password[i + 1]:
            shuffle(result_password)

    return ''.join(result_password)


if __name__ == '__main__':
    main()
