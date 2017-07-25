"""
Determine if two strings are anagrams
"""

def are_anagrams(s1, s2):

    # Compare sorted strings (O(n log n))
    # return sorted(s1) == sorted(s2)

    # Compare character and counts (O(n))
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

print(are_anagrams('rats', 'star'))
print(are_anagrams('rats', 'mice'))

