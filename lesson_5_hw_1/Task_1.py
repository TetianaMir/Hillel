def main():
    isEven = int(input('Введите число: '))
    is_even(isEven)
    print("Результат тестирования: ")
    test()


def is_even(number: int):  # returns boolean value
    """

    @param number: The int value for checking odd or even
    @return: Result of checking
    """
    if number % 2 == 0:
        print('Число четное')
        return True
    else:
        print('Число нечетное')
        return False


def test():
    print("\nПроверка работы функции для числа 10")
    assert is_even(10) is True
    print("Проверка работы функции для числа 1")
    assert is_even(1) is False


main()
