def prime_checking(a):
    primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for x in primes_list:
        if a % x == 0:
            return False
    return True


def list_primes():
    primes_result = []
    for i in range(500, 1000):
        if str(i).startswith("5") and prime_checking(i):
            primes_result.append(i)
    return primes_result


primes_with_5 = list_primes()
print(primes_with_5)
