"""
Solution for a task to generate a random list of integers
"""

import random




def main():
    length = int(input('Enter the list size: '))

    # my_list = []
    # for _ in range(length):
    #    my_list.append(random.randint(1,100))

    my_list = [random.randint(1, 100) for _ in range(length)]

    print(f'Your random generated list of length {length} is:')
    print(my_list)


if __name__ == '__main__':
    main()
