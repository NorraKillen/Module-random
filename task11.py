import copy
import random
a = [input() for _ in range(int(input()))]
b = copy.copy(a)
counter = 0
while counter != len(a):
    random.shuffle(b)
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
for j in range(len(a)):
    print(a[j], '-', b[j])
