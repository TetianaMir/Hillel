def main():
    value = int(input('Введите число: '))
    while value < 1:
        value = int(input('Введите число, которое будет больше либо равен 1!: '))

    print(fibonacci_sequence(value))

    show_result(value)
    print('Тесты для значений')
    test()


def fibonacci_sequence(value):
    """

    @param value: Target position of Fibonacci sequence
    @return: The Fibonacci value
    """
    if value == 0 or value == 1:
        return 0
    elif value == 2:
        return 1
    return fibonacci_sequence(value - 1) + fibonacci_sequence(value - 2)


def test():
    show_result(0)
    assert fibonacci_sequence(0) == 0
    show_result(5)
    assert fibonacci_sequence(5) == 3
    show_result(20)
    assert fibonacci_sequence(20) == 4181


def show_result(value):
    print('Число с последовательности Фибоначчи: ', value, ' = ', fibonacci_sequence(value))


main()
