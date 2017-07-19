"""
Operations involving digits of an integer
"""

import sys

def sum_of_digits(number):
    total = 0

    # For loop
    # for num in str(number):
    #     total += int(num)

    # Using map
    # for num in map(int, str(number)):
    #     total += num

    # Using list comprehension
    for num in [int(i) for i in str(number)]:
        total += num

    return total



def product_of_digits(number):
    product = 1
    for num in str(number):
        product *= int(num)

    return product


def largest_digit(number):
    largest = -sys.maxsize
    for num in str(number):
        if int(num) > largest:
            largest = int(num)

    return largest


def smallest_digit(number):
    smallest = sys.maxsize
    for num in str(number):
        if int(num) < smallest:
            smallest = int(num)

    return smallest


print(sum_of_digits(456))
print(product_of_digits(456))
print(largest_digit(456))
print(smallest_digit(456))
