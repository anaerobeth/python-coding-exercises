def liftoff(count):
    """
    *
    **
    ***
    ****
    *****
    Liftoff!
    """
    # For loop
    # for i in range(1,count+1):
    #     print('*' * (i))

    # While loop
    i = 1
    while i <= count:
        print('*' * (i))
        i += 1

    print('Liftoff!')

def blastoff(count):
    """
    *****
    ****
    ***
    **
    *
    Blastoff!
    """
    # for i in range(count+1 ,1, -1):
    #     print('*' * (i))

    # While loop
    # i = count
    # while i > 0:
    #     print('*' * (i))
    #     i -= 1

    # Recursive

    if count == 0:
        print('Blastoff!')
        return

    print('*' * (count))
    blastoff(count-1)


def factorial(number):
    """
    5! is 5 * 4 * 3 * 2 * 1
    """
    # For loop
    # product = 1
    # for i in range(1, number+1):
    #     product *= i

    # return product

    # Recursive
    if number < 1:
        return 1
    else:
        return number * factorial(number - 1)


liftoff(5)
blastoff(5)
print(factorial(5))
