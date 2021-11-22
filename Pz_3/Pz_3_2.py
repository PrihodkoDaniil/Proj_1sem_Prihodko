# Даны три переменные вещественного типа
# Если их значения упорядочены по взрастанию то удвоить их
# В противном случае заменить на противоположные

while True: # обработка исключений
    try:
        a = float(input("Введите вещественное число: "))
        break
    except ValueError:
        print("Введены неверные данные")

while True: # обработка исключений
    try:
        b = float(input("Введите вещественное число: "))
        break
    except ValueError:
        print("Введены неверные данные")
while True: # обработка исключений
    try:
        c = float(input("Введите вещественное число: "))
        break
    except ValueError:
        print("Введены неверные данные")
if a<b<c:
    a = a * 2
    b = b * 2
    c = c * 2
else:
    a = a * (-1)
    b = b * (-1)
    c = c * (-1)
print(a,b,c)
