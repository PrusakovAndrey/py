# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

path = '/Users/andreyprusakov/Desktop/GB projects/python/Seminar_03/35_task.txt'

def reading (path):
    f = open(path, 'r')
    data = f.read() + ' '
    f.close()
    return data
file = str((reading(path)))

def list_creating (data):
    numbers = []
    while data != '':
        space_pos = data.index(' ')
        numbers.append(int(data[:space_pos]))
        data = data[space_pos+1:]
    return numbers

lst = list_creating(file)
lst = sorted(lst)
print(lst)

def check (list):
    for i in range (len(list)):
        if (list[i] - 1) != list[i-1]:
            res = list[i-1] + 1
    return res
print (check(lst))