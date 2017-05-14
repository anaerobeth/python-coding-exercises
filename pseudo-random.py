# deterministically generate 100 random integers from 1 to 100
import random as random

for i in range(0,100):
    random.seed(i)
    print(random.randint(1, 100))
