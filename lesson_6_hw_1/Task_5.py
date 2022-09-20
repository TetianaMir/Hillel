SIZE_OF_CHESS_BOARD = 8
SEED_WEIGHT = 0.000035


def main():
    value = int(input("Input values in kg: "))
    seed = SEED_WEIGHT
    count_of_seed = value // seed
    print("Count of seeds : ", count_of_seed)
    print("Your seed based on the", some_function(count_of_seed), "cell")


def some_function(count_of_seed):
    ord_list = []
    values_list = [0, 1, 2, 3, 4, 5, 6, 7]
    for i in range(ord('a'), ord('h') + 1):
        ord_list.append(i)

    counter = 0
    while count_of_seed // 2:
        count_of_seed //= 2
        counter += 1

    int_value = counter // SIZE_OF_CHESS_BOARD
    additional_value = counter % SIZE_OF_CHESS_BOARD
    if counter % SIZE_OF_CHESS_BOARD == 0:
        return chr(ord_list[additional_value - 1]) + str(values_list[int_value])
    else:
        return chr(ord_list[additional_value - 1]) + str(values_list[int_value + 1])


main()
