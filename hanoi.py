from stack import Stack

num_discs = 3
tower_a = Stack()
tower_b  = Stack()
tower_c  = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin, end, temp, n):
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
