import random


def main():
    lst = []
    size = int(input('Enter the size of the list: '))
    for i in range(0, size):
        lst.append(random.randint(0, 100))
    print(lst)
    elem = int(input('Enter the desired item: '))

    print(index(lst, elem))


def index(lst, elem):  # returns integer or None
    for i in range(len(lst)):
        if lst[i] == elem:
            return i


if __name__ == '__main__':
    main()
