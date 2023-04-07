import random

num = set()
while len(num) != 7:
    num.add(random.randint(1, 49))

print(*sorted(num))