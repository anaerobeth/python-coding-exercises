"""
Determine if two strings are anagrams

"""

def anagrams1(s1, s2):

    """Compare sorted strings - O(n log n)

    >>> anagrams1('rats', 'star')
    True
    >>> anagrams1('rats', 'mice')
    False
    """

    return sorted(s1) == sorted(s2)


def anagrams2(s1, s2):

    """Compare character and counts - O(m + n)

    >>> anagrams2('rats', 'star')
    True
    >>> anagrams2('rats', 'mice')
    False
    """

    char_count = {}
    for s in s1:
        if s not in char_count:
            char_count[s] = 1
        else:
            char_count[s]  += 1

    for s in s2:
        if s not in char_count:
            return False
        else:
            char_count[s] -= 1

    return all(value == 0 for value in char_count.values())


def anagrams3(s1, s2):

    """Compare dictionaries - O(m + n)

    >>> anagrams3('rats', 'star')
    True
    >>> anagrams3('rats', 'mice')
    False
    """

    from collections import Counter

    return Counter(s1) == Counter(s2)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
