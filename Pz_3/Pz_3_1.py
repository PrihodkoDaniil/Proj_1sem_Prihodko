# Дано целое положительное число
# Проверить истинность высказывания: "Данное число является четным двузначным"

while True: # обработка исключений
    try:
        a = int(input("Введите целое число: "))
        if 10 < a < 100 and (a % 2) == 0:
            print("Истинно")
        else:
            print("Ложно")
    except ValueError:
        print("Введены неверные данные")
        # а можно закрывать проект перед выходом?