def names(file):
    list = []
    f = open(file, "r")
    for i in f:
        list.append(i.split('\t').__getitem__(1))
    return list


print(names("names.txt"))
