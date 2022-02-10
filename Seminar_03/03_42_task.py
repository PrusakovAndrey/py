# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах


# блок распаковки 
path = '/Users/andreyprusakov/Desktop/GB projects/python/Seminar_03/42_coded.txt'
def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

def splitting_to_tuple (a):
    a = a + ' '
    n = '0,1,2,3,4,5,6,7,8,9'
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

path_1 = '/Users/andreyprusakov/Desktop/GB projects/python/Seminar_03/42_decoded.txt'
def writing (path,data):
    f = open(path, 'w')
    f.write(data)
    f.close()

writing(path_1, printing(splitting_to_tuple(reading(path))))

# блок сжатия

line = reading(path_1)
print(line)


def compressing (data):
    data = data + ' '
    count = 0
    res = ''
    for i in range (len(data)-1):
        if data[i] == data[i+1]:
            count +=1
        else:
            res += data[i]+str(count+1)
            count = 0
    return res


print(compressing(line))