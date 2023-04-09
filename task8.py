import random

num = set()
while len(num) != 100:
    num.add(random.randint(1000000, 9999999))
    print(*num, sep='\n')