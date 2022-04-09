# В матрице найти сумму первых двух строк.
from random import randint
i = int(input("Введите количество строк: "))
j = int(input("Введите количество столбцов: "))
matrix = [[randint(-10,10) for y in range(j)] for x in range(i)]
print('Матрица')
for i in matrix:print(*i)
print("Сумма первых двух строк:",sum(matrix[0])+sum(matrix[1]))