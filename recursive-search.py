"""
Given a list of strings and a search term,
find the index of the term in the list if it exists.
If there is no matching term, return -1.
"""

def search(strings, term, index=0):
    if strings[0] == term:
        return index
    if len(strings) <= 1:
        return -1
    return search(strings[1:], term, index=index+1)


search_list = ['apple', 'orange', 'pear', 'fig', 'passionfruit']

assert(search(search_list, 'apple')) == 0
assert(search(search_list, 'foo')) == -1


