"""
Use divide and conquer to implement summation
"""

def summation(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]

    midpoint = len(values) // 2

    return summation(values[:midpoint]) + summation(values[midpoint:])


with open('random_integers.txt', 'r') as f:
    random_integers = [int(line[1:].replace(',', '')) for line in f.readlines()]
    print(random_integers[:5])

print(summation(random_integers))
