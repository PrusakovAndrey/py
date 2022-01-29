# Написать программу преобразования десятичного числа в двоичное

a = int(input('введите число -->> ')) 
def ten2two (a):
    temp = 0
    dd = 0
    array = []
    while a != 1: 
        temp = int(a / 2) 
        dd = a - temp*2 
        array.append(dd) 
        a = temp 
    l = len(array)-1
    ready = [1]
    for i in range (0, l+1):
        ready.append(array[l-i]) 
    return ready
print (ten2two(a))
