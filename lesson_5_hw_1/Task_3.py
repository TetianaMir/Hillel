import math
import random


def main():
    x1 = random.randint(1, 10)
    y1 = random.randint(1, 10)
    r1 = random.randint(1, 10)
    print('First circle: ', x1, y1, r1)
    x2 = random.randint(1, 10)
    y2 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    print('Second circle: ', x2, y2, r2)
    print('Result of the intersection: ', circles_intersect(x1, y1, r1, x2, y2, r2))

    test()


def circles_intersect(x1, y1, r1, x2, y2, r2):  # returns boolean value
    """

    @param x1: Coordinate x first circle
    @param y1: Coordinate y first circle
    @param r1: Radius of first circle
    @param x2: Coordinate x second circle
    @param y2: Coordinate y second circle
    @param r2: Radius of second circle
    @return: Result of intersection
    """
    if x1 == x2:
        if r1 + r2 > abs(y1 - y2):
            return True
        else:
            return False

    elif y1 == y2:
        if r1 + r2 > abs(x1 - x2):
            return True
        else:
            return False
    elif math.pow(r1 + r2, 2) > abs(math.pow(x1 - x2, 2) - math.pow(y1 - y2, 2)):
        return True
    else:
        return False


def test():
    assert circles_intersect(3, 5, 2, 7, 8, 2) is True
    assert circles_intersect(3, 7, 2, 9, 7, 3) is False


main()
