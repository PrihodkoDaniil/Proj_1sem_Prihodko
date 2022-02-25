def low(stroka):
    yield from [i.lower() for i in stroka]
stroka = input("Введите строку: ")
print("".join(low(stroka)))
