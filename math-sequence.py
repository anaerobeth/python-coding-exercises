"""
Collatz conjecture
Print the 3n+1 sequence from n, terminating when it reaches 1.
"""

def generate_sequence(num):
    seq = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1
        seq.append(num)
    return seq


def number_with_longest_chain(limit):
    longest_length = 1
    king = 1
    for i in range(1, limit):
        current_length = len(generate_sequence(i))
        if current_length >= longest_length:
            longest_length = current_length
            king = i
    return king


def main():
    assert generate_sequence(5) == [5, 16, 8, 4, 2, 1]

    assert len(generate_sequence(12)) == 10
    assert len(generate_sequence(19)) == 21
    assert len(generate_sequence(77031)) == 351

    assert number_with_longest_chain(100) == 97

    print(number_with_longest_chain(1000000)) # 837799


if __name__ == '__main__':
    main()
