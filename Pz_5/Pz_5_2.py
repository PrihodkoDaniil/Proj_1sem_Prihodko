# Описать функцию PowerA3(A, B), вычисляющую третью степень числа A и возвращающую ее в переменную B
# (A — входной, B — выходной параметр; оба параметра являются вещественными)
# С помощью этой функции найти третьи степени пяти данных чисел.
def PowerA3(A):
    return pow(A,3)
n=1 # какое число посчету
i=5 # максимальное количество введенных чисел
while n <= i:
    number = float(input())
    B = PowerA3(number)
    n = n + 1
    print(round(B,3))
