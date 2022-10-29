import random


def main():
    list_size = int(input('Введите размер списка: '))
    while list_size < 2:
        print('Нельзя вводить числа < 2\n'
              'Введите число > 2')
        list_size = int(input('Введите размер списка: '))

    min_value = int(input('Введите нижнюю границу списка: '))
    max_value = int(input('Введите верхнюю границу списка: '))

    print("Разница между четными и нечетными значениями: ", diff_odd_even(list_size, min_value, max_value))


def diff_odd_even(num_limit, lower_bound, upper_bound):  # returns int
    list = []

    for item in range(0, num_limit):
        list.append(random.randint(lower_bound, upper_bound))

    print(list)

    sum_even = 0
    sum_odd = 0
    for i in list:
        if i % 2 == 0:
            sum_even = i + sum_even
        else:
            sum_odd = i + sum_odd

    return abs(sum_odd - sum_even)


main()
