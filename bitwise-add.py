from ctypes import c_int32

def bitwise_add(a, b):
    a = c_int32(a).value
    b = c_int32(b).value

    # repeat until there is no carry
    while b != 0:
        carry =c_int32(a & b).value     # common set bits of a and b
        a = c_int32(a ^ b).value        # sum of bits where one is not set
        b = c_int32(carry << 1).value   # shift by 1

    return a

def sum_up(arr):
    total = 0
    for item in arr:
        total = bitwise_add(total, item)

    return total


print(bitwise_add(2, 4))
print(sum_up([1, 2, 5, 10]))
