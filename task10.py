import random
a = [i for i in range(75)]
v = random.sample(a, 25)
v[12] = 0
for i in range(5):
    for j in range(5):
        print(v[0], end=' ')
        del v[0]
    print()