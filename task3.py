import random

length = int(input())
for i in range(length):
    a = chr(random.randint(97, 122))
    v = random.randint(0, 1)
    if v == 0:
        print(a.upper(), end='')
    else:
        print(a, end='')