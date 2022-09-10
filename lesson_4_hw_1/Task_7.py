user_number = input('Enter value: ')


def sum_values(user_numbers):
    if len(user_number) < 3:
        return 0
    sum = 0
    for i in user_numbers:
        sum = sum + (ord(i) - 48)

    return sum


print(sum_values(user_number))
