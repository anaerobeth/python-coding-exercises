def is_palindrome(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False

def longest(string):
    longest = ''
    if is_palindrome(string):
        if len(string) > len (longest):
            longest = string
            return longest
    for i in range(len(string)):
        for j in range(len(string), 1, -1):
            st = string[i:j]
            if is_palindrome(st):
                if len(st) > len(longest):
                    longest = st
    return longest


print(longest('banana'))
print(longest('racecar'))
print(longest('aabcdcb'))
print(longest('forgeeksskeegfor'))

