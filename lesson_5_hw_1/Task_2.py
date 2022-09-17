import math


def main():
    a = int(input('Введите значения а:'))
    b = int(input('Введите значения b:'))
    c = int(input('Введите значения c:'))
    result = solve_quadratic_equation(a, b, c)
    print("Корни уровнения: ", result[0], ' ', result[1])
    test()


def solve_quadratic_equation(a, b, c):  # always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
    """

    @param a: First koef of equation
    @param b: Second koef of equation
    @param c: Third koef of equation
    @return: The tuple of rotes
    """
    D = math.pow(b, 2) - (4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print('Уравнение имеет два решения')
        return x1, x2
    elif D == 0:
        x1 = -b / (2 * a)
        print('Уравнение имеет одно решение')
        return x1, None
    else:
        print('Уравнение не имеет решений')
        return None, None


def test():
    print('Тестирование для чисел: 1, -70, 600 => 60, 10')
    assert solve_quadratic_equation(1, -70, 600) == (60, 10)
    print('Тестирование для чисел: 4, -4, 1 => 0.5, None')
    assert solve_quadratic_equation(4, -4, 1) == (0.5, None)
    print('Тестирование для чисел: 1, 1, 1 => None, None')
    assert solve_quadratic_equation(1, 1, 1) == (None, None)


main()
