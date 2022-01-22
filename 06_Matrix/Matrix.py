# 48 Показать двумерный массив размером m×n заполненный целыми числами
from random import randint
# n, m = int(input('n -->> ')), int(input('m -->> '))
# a = [[randint(-100, 100) for j in range(n)] for i in range(m)]
def print_matrix (array):
    for i in range(len(array)): 
        for j in range(len(array[i])):
            print(array[i][j], end=' ')
        print()
# print_matrix(a)

# 49 Показать двумерный массив размером m×n заполненный вещественными числами
import random
# b = [[round((random.uniform(-10, 10)),2) for j in range(n)] for i in range(m)]
# print_matrix(b)

# 50 В двумерном массиве n×k заменить четные элементы на противоположные
# c = [[0 for j in range(n)] for i in range(m)]
# def change_elements(a):
#     for i in range(len(a)): 
#         for j in range(len(a[i])):
#             if a[i][j] < 0: c[i][j] = - (a[i][j])
#             else: c[i][j] = a[i][j]
# change_elements(a)
# print_matrix(a)
# print_matrix(c)

# 51 Задать двумерный массив следующим правилом: Aₘₙ = m+n
# mat = [[i+j for j in range(n)] for i in range(m)]
# print_matrix(mat)

# 52 В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты
# new_array = [[randint(0,10) for j in range (5)] for i in range (5)]
# print_matrix(new_array)
# print('\n')
# def sqr(a):
#     for i in range (len(a)):
#         for j in range (len(a[i])):
#             if (i % 2 == 0 and j % 2 == 0):
#                 a[i][j] = (a[i][j])**2
#     return (a)
# print_matrix(sqr(new_array))

# print('\n53 В двумерном массиве показать позиции числа, заданного пользователем или указать, что такого элемента нет')
# double = [[ randint(0,10) for j in range (6)] for i in range (6)]
# x = int(input('введите число -->> '))
# def search_position (arr):
#     count = 0
#     for i in range (len(arr)):
#         for j in range (len(arr[i])):
#             if arr[i][j] == x: print('строка -- >> {}, ряд -->> {}'. format (i+1,j+1))
#             else: count += 1
#     if count == 0: print('искомого значения нет в массиве')
# print_matrix(double)
# search_position(double)


# print('\n54 В матрице чисел найти сумму элементов главной диагонали')
# line = [[ randint(0,6) for j in range (3)] for i in range (5)]
# print_matrix(line)
# def diagonal (a):
#     sum = 0
#     for i in range (len(a)):
#         for j in range (len(a[i])):
#             if i == j: sum = sum+a[i][j]
#     return sum
# print(diagonal(line))

# print('\n55 Дан целочисленный массив. Найти среднее арифметическое каждого из столбцов.')
# arr = [[randint(0,10) for i in range (4)] for j in range (4)]
# def average_of_line (a):
#     for i in range (len(a)):
#         av = 1
#         sum = 0
#         for j in range (len(a[i])):
#             sum = sum + a[i][j]
#         av = sum / len(a[i])
#         print('среднее линии {} -->> {}'. format (i, av))
# print_matrix(arr)
# average_of_line(arr)

# 56 Написать программу, которая обменивает элементы первой строки и последней строки
# 57 Написать программу, упорядочивания по убыванию элементы каждой строки двумерной массива.
# 58 Написать программу, которая в двумерном массиве заменяет строки на столбцы или сообщить, что это невозможно (в случае, если матрица не квадратная).
# 59 В прямоугольной матрице найти строку с наименьшей суммой элементов.
# 60 Составить частотный словарь элементов двумерного массива