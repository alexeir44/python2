# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр .
# Пример:
# 67,82 -> 23
# 0,56 -> 11

float_num = input('input float number: ')
print(type(float_num))
sum = 0
for i in float_num:
     if i != '.':
         sum += int(i)
print(sum)


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234) 

n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
     factorial *= i
     print(factorial, end=' ')

# 3. Задать список из n чисел последовательности (1+1/n)^n 
# и вывести на экран их сумму.

from msilib import sequence

n = int(input('Введите число: ')) 

def get_squerence(n):
    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

nums = get_squerence(n)
print(nums)
print(round(sum(nums), 5))



# 4. Реализовать алгоритм перемешивания списка.

import random
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"список после перемешивания:\n{lst}")
 


