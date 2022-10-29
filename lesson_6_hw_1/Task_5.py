SIZE_OF_CHESS_BOARD = 8
SEED_WEIGHT = 0.000035


def main():
    value = int(input("Input values in kg: "))
    seed = SEED_WEIGHT
    count_of_seed = value // seed
    print("Count of seeds : ", count_of_seed)
    print("Your seed based on the", calculate_wheat_chess_position(count_of_seed), "cell")


def calculate_wheat_chess_position(kilograms):
    ord_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    values_list = [0, 1, 2, 3, 4, 5, 6, 7]

    counter = 0
    while kilograms // 2:
        kilograms //= 2
        counter += 1

    int_value = counter // SIZE_OF_CHESS_BOARD
    additional_value = counter % SIZE_OF_CHESS_BOARD
    if counter % SIZE_OF_CHESS_BOARD == 0:
        return str(ord_list[additional_value - 1]) + str(values_list[int_value])
    else:
        return str(ord_list[additional_value - 1]) + str(values_list[int_value + 1])


main()
