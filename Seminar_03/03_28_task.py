# Найти корни квадратного уравнения Ax² + Bx + C = 0
# - Математикой
# - Используя дополнительные библиотеки*

import math
# a = 1
# b = 2
# c = 3
# # d = b**2 - 4*a*c # D<0 - нет корней, D=0 - один корень, D>0 - два различных корня
# def maph (a,b,c): # решение квадратного уравнения x1,2 = (-b +- корень из (b**2 + 4ac)) / 2a
#     x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
#     x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
#     return x1, x2
# print (maph(a,b,c))

# второй способ, используя дополнительные библиотеки 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

def sq_math(a,b,c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x, x 
    else:
        return None, None 
print (sq_math(a,b,c))

