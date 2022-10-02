# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

sizelist = int(input('Введите размер списка: '))
somelist = []
for i in range(sizelist):
    somelist.append(i)
random.shuffle(somelist)
print(somelist)

sumoddel = 0
for i in range(1, sizelist, 2):
    sumoddel += somelist[i]
print('Сумма нечетных элементов списка: ', sumoddel)