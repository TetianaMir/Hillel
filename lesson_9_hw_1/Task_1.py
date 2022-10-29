def internet_domains(file):
    list = []
    f = open(file, "r")
    for i in f:
        list.append(i.replace(".", "").replace("\n", ""))
    return list


print(internet_domains("domains.txt"))
