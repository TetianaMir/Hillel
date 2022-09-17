"""
Task 02. Solution

calculate a formula for given value.

"""
import math


def main():
    a = float(input('Enter value of "a": '))
    b = float(input('Enter value of "b": '))
    c = float(input('Enter value of "c": '))
    pass

    result = (math.log(1 + c) / -b) ** 4 + abs(a)

    print('Yor formula result is:', result)


main()
