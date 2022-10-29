import random


def main():
    list_size = int(input('Введите размер списка: '))
    while list_size < 2:
        print('Нельзя вводить числа < 2\n'
              'Введите число > 2')
        list_size = int(input('Введите размер списка: '))

    min_value = int(input('Введите нижнюю границу списка: '))
    max_value = int(input('Введите верхнюю границу списка: '))

    print("Разница между максимальным и минимальным значением: ", diff_min_max(list_size, min_value, max_value))


def diff_min_max(num_limit, lower_bound, upper_bound):  # returns int
    list = []

    for item in range(0, num_limit):
        list.append(random.randint(lower_bound, upper_bound))

    return max(list) - min(list)


main()
