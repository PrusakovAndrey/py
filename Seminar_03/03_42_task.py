# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

path = '/Users/andreyprusakov/Desktop/GB projects/python/Seminar_03/42_coded.txt'
def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

line = (reading(path))

def splitting_to_tuple (a):
    a = a + ' '
    n = '0,1,2,3,4,5,6,7,9'
    c = ''
    res = []
    r = ''
    for i in range (len(a)):
        if (a[i-1] in n and a[i] not in n and i > 0) or i == len(a):
            c = int(c)
            res.append((r,c))
            c = ''
        if a[i] not in n: r = a[i]
        if a[i] in n: c += a[i]
    return res

def printing (dt):
    str = ''
    for i in range (len(dt)):
        str += dt[i][0]*dt[i][1] 
    return str

print (printing(splitting_to_tuple(line)))