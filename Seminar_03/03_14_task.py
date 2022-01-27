# Подсчитать сумму цифр в вещественном числе.
from random import randint
x = randint(1000,10000)

def sum_of_number (a):
    #print(a)
    b = str(a)
    res = 0
    for i in range (0,len(b)):
        res += int(b[i])
    return (res)
print(sum_of_number(x))