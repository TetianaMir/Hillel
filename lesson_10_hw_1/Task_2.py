from collections.abc import Iterable


def main():
    print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
    test()


def lchain(*iterables):  # returns list
    list = []
    for i in iterables:
        if isinstance(i, Iterable):
            for items in i:
                list.append(items)
    return list


def test():
    assert lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)) == [1, 2, 3, '5', 6, 7, 8, 9]


main()
