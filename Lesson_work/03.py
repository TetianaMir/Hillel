'''
Task 03.  Solution

Find a minimal value for a list of numbers.
'''
from random import randint


def my_min(lst):
    '''
    Finding minimal element for a list.
    '''
    minimal = None
    for elem in lst:
        if (minimal is None) or (elem < minimal):
            minimal = elem

    return minimal


def test_my_min():
    assert my_min([]) is None, 'For empty list the result should be None'
    assert my_min([1, 2, 3]) == 1


def main():
    my_list = [randint(1, 100) for _ in range(10)]
    print('Your list is:')
    print(my_list)

    minimal = my_min(my_list)

    print('Minimal values is: ', minimal)


test_my_min()
main()
