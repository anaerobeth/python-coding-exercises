with open('random_integers.txt', 'r') as f:
    total = 0
    for line in f.readlines():
        total += int(line.replace(',', ''))
print(total)
