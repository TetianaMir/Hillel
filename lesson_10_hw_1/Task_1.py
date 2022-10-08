def deepcopy(values):
    if isinstance(values, list):
        return list(map(deepcopy, values))
    if isinstance(values, tuple):
        return tuple(map(deepcopy, values))
    if isinstance(values, dict):
        return {
            deepcopy(key): deepcopy(values)
            for key, value in values.items()
        }
    return values


phone_book = [
    {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number": "+380501234567"},
    {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number": "+380507654321"},
]
lst1 = ['a', 1, 2.0, ['b']]
lst2 = deepcopy(lst1)
lst1[3].append(phone_book)
print(lst1[3])
print(lst2[3])
