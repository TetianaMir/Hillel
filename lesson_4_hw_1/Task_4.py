def find_next_and_previous_number(value):
    return value + 1, value - 1

number = int(input('Please enter an integer number: '))

values = find_next_and_previous_number(number)

print('Next number for number', number, 'is', str(values[0]) + '.')

print('Previous number for number',  number,  'is', str(values[1]) + '.')