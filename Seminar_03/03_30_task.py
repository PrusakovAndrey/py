# Вычислить число pi c заданной точностью d
# Пример: при d = 0.001, pi = 3.141. 10-1 < d < 10-10, d в диапозоне от 0,1 до 0,0000000001

from decimal import *

print ('3,1415926535')

def pi (t):
    x = 11-len(str(int(t*(10**10))))
    pi = Decimal(0)
    n = 0
    while n < x:
        pi += (Decimal(1)/(16**n))*((Decimal(4)/(8*n+1))-(Decimal(2)/(8*n+4))-(Decimal(1)/(8*n+5))-(Decimal(1)/(8*n+6)))
        n += 1
    pi = int(pi * (10**x))/(10**x)
    return pi
print (pi(0.001))
