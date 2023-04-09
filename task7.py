import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

x = []
for i in matrix:
    for j in i:
        x.append(j)
random.shuffle(x)
for i in range(4):
    for j in range(4):
        matrix[i][j] = x[0]
        del x[0]