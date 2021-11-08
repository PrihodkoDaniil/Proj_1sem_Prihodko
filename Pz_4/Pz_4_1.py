#Дано целое число N
#Используя один цикл, найти сумму 1 + 1/(1!) + 1/(2!) + 1/(3!) + ... +1/(N!)
while True: #Обработка исключений
    try:
        N = int(input("Введите N: "))
        break
    except ValueError:
        print("Неверный формат")
factorial = 1
summ = 1
i = 1
while i <= N:
    factorial *= i
    num = 1/factorial
    i= i+1
    summ+=num
print(round(summ,1))


