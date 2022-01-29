# Подсчитать сумму цифр в вещественном числе.
from random import randint
x = 2.87432

def sum_of_number (a):
    res = 0
    for i in str(a):
        if i != '.': res += int(i)
    return res
print(sum_of_number(x))