# Дан словарь на 6 персон, найти и вывести их средний возраст.
slv={}
i = 0
for i in range(6): # вводим в словарь 6 имен(ключей) и 6 возрастов(значений)
    key = (input("Введите имя: "))
    value = int(input("Введите возраст: "))
    slv[key]= value
    i += 1
print(slv)
print(round(sum(slv.values())/len(slv),2))
