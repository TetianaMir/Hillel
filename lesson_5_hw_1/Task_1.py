def main():
    isEven = int(input('Введите число: '))
    print("Результат чётности для: ", isEven, " == ", is_even(isEven))
    test()


def is_even(number: int):  # returns boolean value
    """

    @param number: The int value for checking odd or even
    @return: Result of checking
    """
    return number % 2 == 0


def test():
    assert is_even(10) is True
    assert is_even(1) is False


main()
