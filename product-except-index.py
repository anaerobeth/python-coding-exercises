"""
Given a list of integers, find the product of every integer
except the integer at that index
"""

from operator import mul
import functools
# from itertools import accumulate


def delete_integer(integers, num):
    copy = integers[:]
    copy.remove(num)
    return copy

def product(integers):
    # python 2 reduce
    # return reduce(mul, integers, 1)

    # python 3 reduce
    # return functools.reduce(operator.mul, integers, 1)

    # using accumulate
    # for value in accumulate(integers, mul):
    #     pass
    # return value

    # python 2 lambda
    # return reduce(lambda x, y: x * y, integers, 1)

    result = 1
    for i in integers:
        result *= i
    return result


def get_products_of_all_ints_except_at_index(integers):
    products = []
    for num in integers:
        new_list = delete_integer(integers, num)
        products.append(product(new_list))
    return products


def get_products_using_division(integers):
    products = []
    # python 2 lambda
    original_product = reduce(lambda x, y: x * y, integers, 1)
    for num in integers:
        if num != 0:
            products.append(original_product / num)
        else:
            products.append(0)
    return products


def get_products_using_greedy_approach(integers):
    products_of_all_ints_except_at_index = [None] * len(integers)

    # find the product of all integers before the index
    product_so_far = 1
    i = 0
    while i < len(integers):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= integers[i]
        i += 1

    # find the product of all integers after the index
    # by walking backwards until index
    product_so_far = 1
    i = len(integers) - 1
    while i >= 0:
        # multiply it with the products list from step above
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= integers[i]
        i -= 1

    return products_of_all_ints_except_at_index



assert(delete_integer([1, 2, 3], 1)) == [2, 3]
assert(product([1, 3])) == 3
assert(get_products_of_all_ints_except_at_index([1, 2, 3])) == [ (2*3), (1*3), (1*2) ]
assert(get_products_using_division([1, 2, 3])) == [ (2*3), (1*3), (1*2) ]
assert(get_products_using_greedy_approach([1, 2, 3, 4])) == [ (2*3*4), (1*3*4), (1*2*4), (1*2*3)]
