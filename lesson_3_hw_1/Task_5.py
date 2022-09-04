#Завдання а)
number = input('Введите число: ')
sum = 0
for num in number:
    if num.isdigit():
        sum = sum + int(num)

print(sum)


#Завдання б)
numb = int(input('Введите число: '))
sum = 0
while numb:
    sum = sum + (numb%10)
    numb = numb//10

print(sum)