import random


def main():
    print("The password was generated successfully:", generate_password())


def generate_symbol_array(start_symbol, end_symbol):
    result_array = []
    for i in range(ord(start_symbol), ord(end_symbol) + 1):
        result_array.append(chr(i))
    return result_array


def get_random_value_from_array(array: list):
    return array.__getitem__(random.randint(0, len(array) - 1))


def generate_password():
    digit_array = generate_symbol_array("0", "9")
    big_letter = generate_symbol_array("A", "Z")
    small_letter = generate_symbol_array("a", "z")
    under_score = "_"
    result_password = ''
    for i in range(0, 8):
        if i % 2 == 0:
            result_password += get_random_value_from_array(digit_array)
        elif i % 3 == 0:
            result_password += get_random_value_from_array(big_letter)
        elif i % 5 == 0:
            result_password += get_random_value_from_array(small_letter)
        else:
            value = random.randint(1, 4)
            if value == 1:
                result_password += get_random_value_from_array(digit_array)
            elif value == 2:
                result_password += get_random_value_from_array(big_letter)
            elif value == 3:
                result_password += get_random_value_from_array(small_letter)
            else:
                result_password += under_score

    return result_password


if __name__ == '__main__':
    main()
