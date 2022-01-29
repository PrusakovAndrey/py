# Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
import re

x = 'AND'
a = ['23456ANDX12', 'bahjnivkaasANDlamvek', '18946yrhjknw']
def check_position (x,a):
    result = [i.start() for i in re.finditer(x, str(a))]
    if len(result) >= 1: 
        return (result[1])
    else: 
        return (False)
print (check_position(x,a))
