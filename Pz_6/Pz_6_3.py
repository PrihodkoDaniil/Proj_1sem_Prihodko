# Дан список A размера N и целое число K (1 < K < 4, K < N ).
# Осуществить циклический сдвиг элементов списка влево на K позиций
# Допускается использовать вспомогательный список из 4 элементов
import random
while True:
    K = int(input("Введите на сколько позиций будет сдвиг: "))
    if 1 < K < 4:
        break
    else:
        print("Данное значеие не входит в указанный радиус")
while True:
    N = int(input("Введите длину списка: "))
    if K < N:
        break
    else:
        print("Список не может быть меньше или равным сдвигу")
A = [] # основной список
i = 0
f = [] # дополнительный список
while i < N:
    A.append(random.randint(0,100))
    i += 1
print("Обычный список: ", A)
for i in range(K): # копируем первые числа, количество зависит от сдвига
    f.append(A[i])
for i in range(len(A)-K): # делаем сдвиг
    A[i]=A[i+K]
for i in range(K): # заменяем дублированные последние числа на первые
    A[i-K]=f[i]
print("Сдвинутый список: ", A)