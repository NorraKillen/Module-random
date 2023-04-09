import random

n = 10**6

k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x**2 + y**2 < 1:
        k += 1

print((k/n)*s0)