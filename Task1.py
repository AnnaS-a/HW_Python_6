# Задача:Реализуйте алгоритм перемешивания списка.
from array import array
import random
import copy
n = int(input('Введите число n - количество чисел последовательности: '))

# array = []
# for i in range(n):
#     array.append(i + 1)

array = list(range(1, n + 1))
array1 = copy.deepcopy(array)
random.shuffle(array1)
print('Первоначальный список', array)
print('Перемешанный список', array1)
