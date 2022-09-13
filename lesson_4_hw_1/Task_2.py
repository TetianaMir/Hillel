import math


def triangle_square_and_perimeter(a, b):  # returns 2 values\
    square = 0.5 * (a * b)
    perimeter = math.sqrt((a * a) + (b * b)) + a + b
    return square, perimeter

print(triangle_square_and_perimeter(3,4))