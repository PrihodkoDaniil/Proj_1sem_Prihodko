# Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний.
def low(stroka):
    yield from [i.lower() for i in stroka]
stroka = input("Введите строку большими буквами: ")
print("".join(low(stroka)))
