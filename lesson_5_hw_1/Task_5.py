def main():
    value = int(input('Введите значение: '))
    show_result(value)
    print('Тесты для значений')
    test()


def function_sing(x):
    """

    @param x: Value for checking
    @return: integer value after sign check second(1 when value bigger than 0,
                                                   0 when value equals to 0,
                                                  -1 when value less than 0)
    """
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1


def test():
    show_result(1)
    assert function_sing(1) == 1
    show_result(0)
    assert function_sing(0) == 0
    show_result(-1)
    assert function_sing(-1) == -1


def show_result(value):
    print('sing для значения ', value, ' = ', function_sing(value))


main()
