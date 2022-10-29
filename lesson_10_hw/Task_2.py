import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:

    def __init__(self, inner_x, inner_y, circle_radius):
        self.inner_x = inner_x
        self.inner_y = inner_y
        self.circle_radius = circle_radius

    def calculate(self, point: Point):
        calculation_x = math.pow(point.x - self.inner_x, 2)
        calculation_y = math.pow(point.y - self.inner_y, 2)

        return calculation_x + calculation_y <= math.pow(self.circle_radius, 2)


def main():
    point = Point(2, 1)
    circle = Circle(2, 2, 2)
    print(circle.calculate(point))

    point_2 = Point(1, 1)
    circle_2 = Circle(5, 1, 1)
    print(circle_2.calculate(point_2))


if __name__ == '__main__':
    main()
