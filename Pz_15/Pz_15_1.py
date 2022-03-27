# Сгенерировать матрицу на произвольное количество элементов,в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.
from random import randint
i = int(input("Введите количество строк: "))
j = int(input("Введите количество столбцов: "))
B = [[randint(-10,10) for y in range(j)] for x in range(i)]
for i in B:
    print(*i)
for i in range(len(B)):
    for j in range(len(B[i])-1):
        B[i][j+1] += B[i][j]
for i in B:
    print(*i)