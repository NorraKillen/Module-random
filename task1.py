import random

n = int(input())

for i in range(n):
    a = random.randint(0, 1)
    if a == 0:
        print('Решка')
    else:
        print('Орел')