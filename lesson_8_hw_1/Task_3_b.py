# original list
list = [472, 326, 1, '1101000', 9, '20', 863, '0']
n_list = [int(item) for item in list]

print(sorted(n_list, key=str))
