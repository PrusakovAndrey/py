# https://docs.google.com/presentation/d/1QlQIv5iRR9-CBc_o2lVlfM1lZdbbXBz_1f3SyOk1q3s/edit#slide=id.g10568cc951e_0_238


# a = 123
# b = 1.23
# print(a)
# print(b)
# value = None # None создает переменную с пустым значением
# value = 345
# print(value)
# print(type(value)) # определение типа данных благодаря type
# s = 'qwerty и \n"" ковычки ' # комментирование происходит с помощью решетки, перенос на другу строку благодаря \n
# print (s)

import random
a = random.randint(0,22)
print(a)

# def count_numbers (n):
#     for i in range (0,n+1):
#         if i % 2 == 0: print(i)
# count_numbers(10)

# print('\n29 Произведение чисел от 1 до N')
def prois(n):
    res = 1
    for i in range (1,n+1): res = res*i
    return res
print(prois(5))

