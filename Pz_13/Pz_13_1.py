# В последовательности на n целых чисел умножить все элементы на последний минимальный элемент.
from random import randint
S=[randint(-9,9)for i in range(int(input("Введите размер последовательности: ")))]
print("Исходная послдеовательность:",S,"Конечная последовательность:",list(map(lambda x: x*min(S),S)))
