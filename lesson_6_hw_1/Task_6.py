def main():
    first_symbol = input('Enter first symbol: ')
    last_symbol = input('Enter last symbol: ')

    print(sum_symbol_codes(first_symbol, last_symbol))


def sum_symbol_codes(first, last):  # returns int
    sum_symbols = 0

    if ord(first) > ord(last):
        first, last = last, first

    for i in range(ord(first), ord(last) + 1):
        sum_symbols += i

    return sum_symbols


main()
