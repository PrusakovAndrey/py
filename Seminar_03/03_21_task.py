# Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

x = 'AND'
a =['AND', 'b jkasnc', 'and', 'bahfdjcn', 'AND', 'and']

def searching (x,a):
    count = 0
    for i in range (len(a)):
        if a[i] == x: count +=1
        if count == 2:
            return ([i])
    else: return ('not found')

print(searching(x,a))