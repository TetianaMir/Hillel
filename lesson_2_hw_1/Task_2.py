import math

a = int(input('Введите значение переменной а: '))

while a == 0:
    a = int(input('Введите значение переменной а, которая будет > 0: '))

b = int(input('Введите значение переменной b: '))
c = int(input('Введите значение переменной c: '))
sub_formula = 4 * a * c
x1 = -b + (math.sqrt(math.pow(b, 2) - sub_formula)) // (2 * a)
x2 = -b - (math.sqrt(math.pow(b, 2) - sub_formula)) // (2 * a)

print('Результат решения x1: ', x1)
print('Результат решения x2: ', x2)
