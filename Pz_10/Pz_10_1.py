# Средствами языка Python сформировать текстовый файл (.txt),
# содержащий поледовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемуб обработку элементов:
# Исходные данные:
# Количество элементов:
# Произведение элементов:
# Количество пар, для которых произведение элементов делится на 3
# (элементы пары в последовательности являются соседними):
I = ['-5 -4 -3 -2 -1  1  2  3  4  5']
f1 = open("Firsttask.txt", "w")
f1.writelines(I)
f1.close()
f2 = open("Secondtask.txt","w")
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(I)
f2.close
f1 = open("Firsttask.txt")
k = f1.read()
k = k.split()
for i in range (len(k)):
    k[i] = int(k[i])
f1.close
f1 = open("Firsttask.txt")
pro, t = 1, 0
for i in range(len(k)):
    pro *= k[i]
    if (k[i]*k[i-1])%3 == 0 :
        t +=1
f2 = open("Secondtask.txt","a")
f2.write('\n')
print('Количество элементов:',len(k),
      '\nПроизведение элементов:',pro,
      '\nКоличество пар:',t, file=f2)
f2.close()