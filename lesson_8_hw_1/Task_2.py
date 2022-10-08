import copy


def copydeep(array):
    new_array = []
    for i in array:
        if isinstance(i, list):
            new_array.append(copydeep(i))
        else:
            new_array.append(i)
    return new_array


lst1 = ['a', 1, 2.0, ['b']]
lst2 = copydeep(lst1)
lst1[3].append(0)
print(lst1[3], lst2[3])  # ['b', 0] ['b']
