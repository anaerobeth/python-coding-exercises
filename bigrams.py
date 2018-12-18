"""


"""

ngrams = []

def count_words(string):
    count = 0
    for c in string:
        if c == ' ':
            count += 1
    count = count + 1 if count > 0 else count

    return count

def count_ngrams(string, n):
    # ngrams only occur in the same phrase or sentence
    punctuations = list('.,!;:?-')
    count = 0
    words = 0
    for c in string:
        if c == ' ':
            words += 1
        if c in punctuations:
            if words > 0:
                count += words - 1
            words = 0

    count = count + 1 if count > 0 else count

    return count
