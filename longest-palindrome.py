def is_palindrome(string):

    """
    Base case is 1 - a char is a palindrome of itself
    Remove one letter from each end and recursively compare

    >>> is_palindrome('banana')
    False
    >>> is_palindrome('racecar')
    True
    """

    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False


def longest_palindrome(string):

    """
    Loop through from both ends of string to create substrings
    of decreasing length, record longest palindromic substring
    Until current longest exceeds longest possible palindrome in the loop

    >>> longest_palindrome('')
    'Empty string'
    >>> longest_palindrome('aabcdcb')
    'bcdcb'
    >>> longest_palindrome('forgeeksskeegfor')
    'geeksskeeg'
    >>> longest_palindrome(14545451)
    '45454'
    """

    # Handle empty string or numeric inputs
    if string is '':
        return 'Empty string'
    else:
        string = str(string)

    if is_palindrome(string):
        return string

    longest = ''
    cap = len(string)

    for i in range(len(string)):
        # Length of longest possible palindrome decreases with each loop
        cap -= 1
        for j in range(len(string), 1, -1):
            st = string[i:j]
            if is_palindrome(st) and (len(st) > len(longest)):
                longest = st
            # Stop when longest exceeds the cap
            if len(longest) > cap:
                return longest


if __name__ == '__main__':
    import doctest
    doctest.testmod()
