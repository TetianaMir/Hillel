def gen_primes():
    array = []
    for curItem in range(1, 101):
        prime = curItem > 1 and (curItem % 2 != 0 or curItem == 2) and (curItem % 3 != 0 or curItem == 3)
        y = 5
        d = 2
        while prime and y * y <= curItem:
            prime = curItem % y != 0
            y += d
            d = 6 - d

        if prime:
            array.append(curItem)
    return array


print(gen_primes())
