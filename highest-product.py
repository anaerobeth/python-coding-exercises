"""
Given a list of positive integers, find the highest product
you can get from three of the integers
"""

import sys

def highest_product(integers):
    # only works if all integers are positive
    min_val = -sys.maxsize
    top_one, top_two, top_three = min_val, min_val, min_val
    for num in integers:
        if num > top_one:
            top_three, top_two, top_one = top_two, top_one, num
        elif num > top_two:
            top_three, top_two = top_two, num
        elif num > top_three:
            top_three = num

    return top_one * top_two * top_three


assert(highest_product([1, 2, 3, 4])) == 24

