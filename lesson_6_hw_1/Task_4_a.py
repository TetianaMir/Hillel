import random


def main():
    number = str(random.randint(100000000000, 999999999999))
    print(number)
    print(get_max_digit(number))


def get_max_digit(number):
    etalon = 0
    for i in number:
        if int(i) > etalon:
            etalon = int(i)

    return etalon


main()
