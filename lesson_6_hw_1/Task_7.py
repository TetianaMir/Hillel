import random


def main():
    number = random.randint(1, 10)
    user_number = int(input('Enter a number: '))
    guess_the_number(number, user_number)


def guess_the_number(number, user_number):
    if user_number == number:
        print('Congratulation!')
    else:
        while user_number != number:
            if user_number > number:
                print('Your number bigger than target')
                user_number = int(input('Enter a number: '))
            elif user_number < number:
                print('Your number smaller than target')
                user_number = int(input('Enter a number: '))

        print('Congratulation!')


if __name__ == '__main__':
    main()
