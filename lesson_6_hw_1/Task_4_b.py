import random


def main():
    number = random.randint(100000000000, 999999999999)
    print(number)
    print('Максимальная цифра:', get_max_digit(number))


def get_max_digit(number: int):
    list = []
    while number:
        list.append(number % 10)
        number = number // 10

    return max(list)


main()
