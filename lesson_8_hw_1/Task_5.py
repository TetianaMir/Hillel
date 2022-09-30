def gen_primes(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    y = 5
    d = 2
    while prime and y * y <= num:
        prime = num % y != 0
        y += d
        d = 6 - d
    return prime


print(*[i for i in range(101) if gen_primes(i)])
