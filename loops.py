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


liftoff(5)
blastoff(5)
