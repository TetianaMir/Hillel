import pickle

running = True

# ------------------------------------------------------------------------------
phone_book = [
    {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number": "+380501234567", "profile": "petr_pert"},
    {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number": "+380507654321", "profile": "ivan_i" },
    {"name": "Maksym", "surname": "Yena", "age": 23, "phone_number": "+380501234567", "profile": "maksym_ye"}
]


# ------------------------------------------------------------------------------
def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print("| Inst:    %20s |" % entry["profile"])


# ------------------------------------------------------------------------------
def print_phonebook():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


# ------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name = input("    Enter name: ")
    age = int(input("    Enter age: "))
    phone_number = input("    Enter phone num.: ")
    inst = input("    Enter Instagram: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["profile"] = inst

    phone_book.append(entry)


# ------------------------------------------------------------------------------
def printError(message):
    print("ERROR: %s" % message)


# ------------------------------------------------------------------------------
def printInfo(message):
    print("INFO: %s" % message)


# ------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


# ------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


# ------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name = str(input("    Enter name: "))
    found = False
    for i in range(len(phone_book)):
        if phone_book[i]["name"] == name:
            found = True
            del phone_book[i]
            print_phonebook()
    if not found:
        printError("Not found!!")


# ------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


# ------------------------------------------------------------------------------
def print_phonebook_by_age():
    print("Sort by age: ", sorted(phone_book, key=lambda item: item["age"]))


# ------------------------------------------------------------------------------
def increase_age():
    k = int(input("    Enter koef for age: "))
    for person in phone_book:
        person["age"] += k
    print_phonebook()


# ------------------------------------------------------------------------------
def avr_age_of_all_persons():
    all_age = [person["age"] for person in phone_book]
    average = sum(all_age) // len(all_age)
    print(average)


# ------------------------------------------------------------------------------
def sort_by_name():
    phone_book.sort(key=lambda item: item["name"])
    print_phonebook()

# ------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")

# ------------------------------------------------------------------------------
def inst_profile():
    profile = str(input("    Enter Instagram profile: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["profile"] == profile:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


# ------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


# ------------------------------------------------------------------------------
def exit():
    global running
    running = False


# ------------------------------------------------------------------------------
def print_prompt():
    print()
    print()
    print()
    print("~ Welcome to phonebook ~")
    print("Select one of actions below:")
    print("     1 - Print phonebook entries")
    print("     2 - Print phonebook entries (by age)")
    print("     3 - Add new entry")
    print("     4 - Find entry by name")
    print("     5 - Find entry by age")
    print("     6 - Delete entry by name")
    print("     7 - The number of entries in the phonebook")
    print("     8 - Avr. age of all persons")
    print("     9 - Increase age by num. of years")
    print("     10- Sort by name")
    print("     11- Instagram profile")
    print("     s - Save to file")
    print("     l - Load from file")
    print("     0 - Exit")
    print()


# ------------------------------------------------------------------------------
def main():
    while running:
        try:

            menu = {
                '1': print_phonebook,
                '2': print_phonebook_by_age,
                '3': add_entry_phonebook,
                '4': find_entry_name_phonebook,
                '5': find_entry_age_phonebook,
                '6': delete_entry_name_phonebook,
                '7': count_all_entries_in_phonebook,
                '8': avr_age_of_all_persons,
                '9': increase_age,
                '10': sort_by_name,
                '11': inst_profile,
                '0': exit,
                's': save_to_file,
                'l': load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
