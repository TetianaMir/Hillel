import math


def cone_square_and_volume(radius, height):  # returns 2 floats
    s_base = math.pi * math.pow(radius, 2)
    l = math.sqrt((math.pow(radius, 2) + math.pow(height, 2)))
    s_right = math.pi * radius * l
    square = s_base + s_right

    volume = 1 / 3 * math.pi * math.pow(radius, 2) * height
    return square, volume


radius = int(input('Введите значение радиуса: '))
height = int(input('Введите значение высоты: '))

values = cone_square_and_volume(radius, height)
print('Площадь = ' + str(values[0]))
print('Объем = ' + str(values[1]))
