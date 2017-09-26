from itertools import chain

def unary(a):
    return ''.join(['a' for _ in range(abs(a))])

def plus(a, b):
    if a > 0 and b > 0:
        return len(list(chain(unary(a),unary(b))))

    if a < 0 and b < 0:
        a, b = -a, -b
        return -len(list(chain(unary(a),unary(b))))

    if abs(a) == abs(b):
        return 0

    if abs(a) < abs(b):
        a, b = b, a

    temp = list(unary(a))
    for i in range(abs(b)):
        temp.pop()
    return len(temp)

print(plus(2, 4))
print(plus(-2, -5))
print(plus(-2, 5))
print(plus(2, -5))
print(plus(-5, 5))
print(plus(0, 0))
