# Дан список размера N.
# Найти номера двух ближайших элементов из этого списка
# Вывести эти номера в порядке
import random
import math
N = int(input("Введите размер списка: "))
a = [] # основной список
b = [] # дополнительный список
i = 0
while i < N:
    a.append(random.randint(0,100))
    i += 1
print(a)
for i in range(len(a)-1):
    g = abs(a[i]-a[i+1]) # находим разность чисел по парам
    b.append(g)
    f = min(b)
    if abs(a[i]-a[i+1]) == f:
        k = a[i]
        k2 = a[i+1]
        index1 = a.index(k)
        index2 = a.index(k2)
print("Минимальная разность: ", f)
print("числа из которых получена минимальная разность: ", k, k2)
if index1 < index2:
    print("Номера этих двух чисел: ", index1, index2)
else:
    print("Номера этих двух чисел: ", index2, index1)