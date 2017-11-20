def count_chars(word):
    chars = {}
    for c in word:
        chars.setdefault(c, 0)
        chars[c] += 1

    return chars

print(count_chars('supercalifragilisticexpialidocius'))


