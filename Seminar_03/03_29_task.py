# Найти НОК (наименьшее общее кратное) двух чисел
import math

n = 14
m = 21
def nok (a,b):
    return ((a * b) / math.gcd(a , b)) # gcd - НОД (наибольший общий делитель)

print(nok(n,m))
