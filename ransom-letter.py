"""
Given string R (the ransom letter) and string N (the newspaper),
can R can be written entirely from cutout letters from N?
"""

def simple_ransom(ransom, news):

    """Loop through each element in r and check if it is in n
    Only works if all letters are unique
    f =: { False if l(n) == 0 or ln(r) > ln(n); True if [R] in [N] else False }

    >>> simple_ransom('pay me', 'pay pay')
    False
    >>> simple_ransom('pay me', 'payyyyy meee')
    True
    """

    if len(news) == 0 or len(ransom) > len(news):
        return False
    return all(x in news for x in ransom)


def to_dict(s):
    return { k:v for k, v in enumerate(s)}


def ransom_dict(ransom, news):

    """ 
    For each key in r dict, check if key is in n dict
    Check if the count values are greater in n than r

    f(r,n) := { for k, v in r: True if nk, nv > v else False }
    >>> ransom_dict('pay me', 'payyyyy meee')
    True
    >>> ransom_dict('pay me', 'pay pay')
    False
    >>> ransom_dict('payyyyy meee', 'pay me')
    False
    >>> ransom_dict('pay me', '')
    False
    """

    rdict = to_dict(ransom)
    ndict = to_dict(news)

    for k, v in rdict.items():
        if k not in ndict:
            return False
        elif ndict[k] < v:
            return False

    return True


def ransom_charmap(ransom, news):

    """
    Assuming all chars are ASCII, we can hold their counts in a charmap array
    Create the array from r then check if n has the required number of chars
    Adapted from https://www.pramp.com/tryout

    >>> ransom_charmap('pay me', 'payyyyy meee')
    True
    >>> ransom_charmap('pay me', 'pay pay')
    False
    >>> ransom_charmap('payyyyy meee', 'pay me')
    False
    >>> ransom_charmap('pay me', '')
    False
    """

    charmap = [0] * 256
    charcount = 0

    for char in ransom:
        index = ord(char)
        # ignore blank space
        if index != 32:
            charcount +=1
            if charmap[index] == 0:
                charmap[index] = 1
            else:
                charmap[index] += 1

    for char in news:
        index = ord(char)
        # ignore blank space
        if index != 32:
            if charmap[index] > 0:
                charmap[index] -= 1
                charcount -= 1
            if charcount == 0:
                return True

    return False


if __name__ == '__main__':
    import doctest
    import pdb


    doctest.testmod()
