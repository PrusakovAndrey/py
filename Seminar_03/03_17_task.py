# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

from random import randint
def list_create (n):
    l = list()
    for i in range (0,n):
        a = randint(-n,n)
        l.append(a)
    return(l)
def file_to_list (path):
    data = open(path, 'r')
    input_data = list()
    for d in data:
        input_data.append(int(d))
    data.close()
    return (input_data)
def function (lt, fl):
    res = 1
    for j in range (0,len(lt)):
        temp_index = lt[j]
        res *= fl[temp_index]
    return (res)

lt = file_to_list('file.txt')
print(lt)
fl = list_create(15)
print(fl)
print(function(lt,fl))

