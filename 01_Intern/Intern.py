# Почувствуй себя интерном*

# 01_Вывести квадрат числа
# 02_По двум заданным числам проверять является ли первое квадратом второго
# 03_Даны два числа. Показать большее и меньшее число
# 04_По заданному номеру дня недели вывести его название
# 05_Найти максимальное из трех чисел
# 06_Написать программу вычисления значения функции y = f(a)
# 07_Выяснить является ли число чётным
# 08_Показать числа от -N до N
# 09_Показать четные числа от 1 до N
# 10_Показать последнюю цифру трёхзначного числа
# 11_Показать вторую цифру трёхзначного числа
# 12_Дано число из отрезка [10, 99]. Показать наибольшую цифру числа
# 13_Удалить вторую цифру трёхзначного числа
# 14_Выяснить, кратно ли число заданному, если нет, вывести остаток.
# 15_Найти третью цифру числа или сообщить, что её нет

# print ('01_Вывести квадрат числа')
# a = 5
# print (a**2)

# #_______________________________________________
# print('\n02_По двум заданным числам проверять является ли первое квадратом второго')
# a = int(input('a = '))
# b = int(input('b = '))
# if (a**2 == b):
#     print ('Да, a является квадратом b')
# else:
#     print ('Нет, a не ялвяется квадратом b')

#_______________________________________________
# print ('\n03_Даны два числа. Показать большее и меньшее число')
# a = 9
# b = 7
# if (a > b):
#     print ('a равно {} и больше b, равного {}'.format (a, b))
# else:
#     print ('b равно {} и больше a, равного {}'. format (b, a))

#_______________________________________________
# print ('\n# 04_По заданному номеру дня недели вывести его название')
# list = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# day = int(input('введите номер дня недели - :'))
# if (day in range (1,7)):
#     print (list[day-1])
# else:
#     print ('вы ввели значение не из диапозона от 1 до 7')

#_______________________________________________
# print('\n# 05_Найти максимальное из трех чисел')
# a = 25
# b = 47
# c = 12
# m = max(a,b,c)
# print('a = {}, b = {}, c = {} \nmax is - {}'.format(a,b,c,m))

#_______________________________________________
from random import randint, random


print ('\n06_Написать программу вычисления значения функции y = f(a)')

#_______________________________________________
# print ('\n07_Выяснить является ли число чётным')
# a = int(input('a = '))
# if (a%2 == 0):
#     print('a - четное')
# else:
#     print('a - нечетное')

#_______________________________________________
# print('\n08_Показать числа от -N до N')
# a = int(input('введите минимальное значение :'))
# b = int(input('введите максимально значение :'))
# c = range(a,b)
# for i in c:
#     print (c)

#_______________________________________________
# print('\n09_Показать четные числа от 1 до N')
# for i in range(0,10):
#     if (i % 2 == 0):
#         print(i)

#_______________________________________________
# print('\n10_Показать последнюю цифру трёхзначного числа')
# a = 331
# print(a%10)

#_______________________________________________
# print('\n11_Показать вторую цифру трёхзначного числа')
# a = 453
# print(int((a/10)%10))

#_______________________________________________
# print('\n12_Дано число из отрезка [10, 99]. Показать наибольшую цифру числа')
# a = randint(10,99)
# print(a)
# f = int(a/10)
# s = a%10
# print(max(f,s))

#_______________________________________________
# print('\n# 13_Удалить вторую цифру трёхзначного числа')
# a = 238
# print(int((a-a%100)/10+a%10))

#_______________________________________________
# print('\n14_Выяснить, кратно ли число заданному, если нет, вывести остаток.')
# a = 45
# print ('a =',a)
# b = int(input('b = '))
# if (a%b == 0):
#     print('a кратно b')
# else:
#     print('a не кратно b, остаток равен', a%b)

#_______________________________________________
# print('\n15_Найти третью цифру числа или сообщить, что её нет')
# a = randint(0,10000)
# print ('случайное число = ', a)
# if (a<100):
#     print('у числа нет третьей цифры')
# else:
#     s = str(a)
#     print(s[2])