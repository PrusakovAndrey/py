# Почувствуй себя лидом*

# Выяснить являются ли три числа сторонами треугольника
# Определить сколько чисел больше 0 введено с клавиатуры
# Написать программу преобразования десятичного числа в двоичное
# Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы
# Показать числа Фибоначчи
# Написать программу масштабирования фигуры
# Тут для тех кто далеко улетел, чтобы задавались вершины фигуры списком (одной строкой)
# например: "(0,0) (2,0) (2,2) (0,2)"
# коэффициент масштабирования k задавался отдельно - 2 или 4 или 0.5
# В результате показать координаты, которые получатся.
# при k = 2 получаем "(0,0) (4,0) (4,4) (0,4)"
# Написать программу копирования массива

# print('\nВыяснить являются ли три числа сторонами треугольника')
# print ('введите координтаы точки А')
# ax = int(input('x = '))
# ay = int(input('y = '))
# print ('введите координтаы точки B')
# bx = int(input('x = '))
# by = int(input('y = '))
# print ('введите координтаы точки C')
# cx = int(input('x = '))
# cy = int(input('y = '))
# if (ax - bx) * (cy - by) - (cx - bx) * (ay - by) == 0:
#     print ('точки расположены на прямой и не являются вершинами треугольника')
# else:
#     print ('точки расположены не на одной прямой, а значит через них можно построить треугольник')

# print ('\nОпределить сколько чисел больше 0 введено с клавиатуры')
# print ('введите сколько угодно чисел через пробел')
# array = [int(i) for i in input().split()]
# print(array)
# count = 0
# for i in range (0, len(array)):
#     if (array[i] > 0):
#         count += 1
# print(count)

# print('\nНаписать программу преобразования десятичного числа в двоичное')
# a = int(input('введите число -->> ')) # 12
# temp = 0
# dd = 0
# array = []
# while a != 1: 
#     temp = int(a / 2) 
#     dd = a - temp*2 
#     array.append(dd) 
#     a = temp 
# l = len(array)-1
# ready = [1]
# for i in range (0, l+1):
#     ready.append(array[l-i]) 
# print(ready)

# print('\nНайти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы')
# b1 = 2
# k1 = -1
# b2 = -3
# k2 = 1
# x = round((k2 - k1) / (b1 - b2),2)
# y = round(b2 * x + k2,2)
# print (x, y)

# print('\nПоказать числа Фибоначчи')
# n = int(input('введите границу - '))
# a = 0
# b = 1
# print (a)
# print (b)
# for i in range (0, n):
#     c = a + b
#     print(c)
#     a = b
#     b = c

# print('\nНаписать программу масштабирования фигуры')
# a = str(input('введите координаты точек в формате ХХ,ХХ ХХ,ХХ -->> ')+' ')
# array = []
# k = int(input('введите коэфициент масштабирования фигуры -->> '))
# def coordinates(a):
#     l = len(a)
#     temp_number = str()
#     for i in range (0,l):
#         if (a[i] >= '0' and a[i] <= '9'):
#             temp_number += a[i]
#         else:
#             array.append(int(temp_number))
#             temp_number = str()
#     return (array)
# coordinates(a)
# print (array)
# def scaling (array, k):
#     result = ' '
#     l = len(array) 
#     for i in range (0, l):
#         if i % 2 == 0:
#             result = result + '(' + str(array[i]*k) + ','
#         elif i % 2 != 0:
#             result = result + str(array[i]*k) + ') '
#     return(result)
# print(scaling(array,k))

print('\nНаписать программу копирования массива')
a = [0,1,3,7,9]
print(a,'\n')
def array_copy (a):
    new_array = []
    for i in range (0, len(a)):
        new_array.append(a[i])
    return new_array
print(array_copy(a))
