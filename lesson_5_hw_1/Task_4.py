def main():
    value = int(input('Введите год : '))
    while value == 0:
        value = int(input('Если хотите выйти введите: -1\nВведите год > 0: '))
        if value == -1:
            exit(0)

    print('Высокосный ли', value, ":", check_year(value))
    test()


def check_year(year: int):
    """

    @param year: Target year for calculation
    @return: Boolean result of verifying of the leap year or not
    """
    if (year % 100 != 0 or year % 400 == 0) and (year % 4 == 0):
        return 'YES'
    else:
        return 'NO'


def test():
    assert check_year(1601) == 'NO'
    assert check_year(1920) == 'YES'


if __name__ == '__main__':
    main()
