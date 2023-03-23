import random

matrix = [[random.randint(0,100) for x in range(4)] for y in range(4)]
print(matrix)

list = [matrix[x][x] for x in range(4)]
print(list)