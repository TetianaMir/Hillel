# original list
list = [472, 326, '99', 1, '1101000', 9, '20', 863, '0', '999']


def compare_by_first_symbol(currentItem):
    currentItem = str(currentItem)
    return str(currentItem[0])


print(sorted(list, key=compare_by_first_symbol))
