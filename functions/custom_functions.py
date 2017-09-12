from mergesort import sorter

def average(values):
    """ Return the average of values in an array"""
    return sum(values) / len(values)


def mode(given):
    """ Return the most frequent value in a given array"""
    arr = sorter(given)
    mode = arr[0]
    longest_run = 0
    runs = 0

    for n in range(len(arr)-1):
        if n < len(arr):
            diff = abs(arr[n] - arr[n+1])

            if diff == 0:
                runs += 1
                if longest_run < runs:
                    longest_run = runs
                    mode = arr[n]
            else:
                run = 0
    return mode


def gcd(a, b):
    """Return the greatest common denominator """
    while a % b != 0:
        a, b = b, a % b
    return b
