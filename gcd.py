def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

assert(gcd(12, 16)) == 4
