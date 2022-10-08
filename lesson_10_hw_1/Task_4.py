def main():
    list = ['Yan Aim', 'Zara Zmith', 'John Tnow', 'Potter Pin']
    print(group_by_surname(list))


def group_by_surname(list_of_enrollees):  # returns 4 ints
    groups = {
            "A-I": 0,
            "J-P": 0,
            "Q-T": 0,
            "U-Z": 0,
            }
    for user in list_of_enrollees:
        name, surname = user.split()
        if 'A' <= surname[0] <= 'I':
            groups["A-I"] += 1
        elif 'J' <= surname[0] <= 'P':
            groups["J-P"] += 1
        elif 'Q' <= surname[0] <= 'T':
            groups["Q-T"] += 1
        else:
            groups["U-Z"] += 1

    return groups.values()


if __name__ == '__main__':
    main()