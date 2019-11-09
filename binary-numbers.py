"""
Generate binary numbers up to n

"""

from queue import Queue


def generate_binary_nums(n, start=1):

    """Returns binary numbers from start up to n
    >>> generate_binary_nums(3)
    [1, 10, 11]

    >>> generate_binary_nums(5, start=1)
    [1, 10, 11, 100, 101]

    >>> generate_binary_nums(6, start=3)
    [11, 100, 101, 110]
    """

    queue = Queue()
    queue.enqueue(1)
    result = []

    for i in range(n):
        # Remove front element from queue and append to result
        result.append(str(queue.dequeue()))

        # Create two strings by appending 0 or 1 to front element
        # Add back the two strings to the queue
        queue.enqueue(int(result[i] + '0'))
        queue.enqueue(int(result[i] + '1'))

    binary_nums = map(lambda x: int(x), result)
    return binary_nums[start-1:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
