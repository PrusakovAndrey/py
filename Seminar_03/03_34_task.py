# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.
from dataclasses import replace
from re import X
from unicodedata import digit
path1 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom1.txt'
path2 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom2.txt'

def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

p1 = reading(path1)
p2 = reading(path2)

def parsing (dt):
    ls = ['+', '-']
    res = ''
    for i in range (0,len(dt)):
        if dt[i] == '+': 
            res += ','
        elif dt[i] == '-': 
            res +=',' + dt[i]
        elif dt[i] == '=':
            res += ','+dt[i]
        else: 
            res += dt[i]
    r = res.replace(' ', '')
    r = r.split(',')
    return r

p_p1 = parsing(p1)
p_p2 = parsing(p2)
print(p_p2)

def get_tuple (data):
    t = ''
    r = set()
    for i in range (0, len(data)):
        for j in range (0, len(data[i])):
            if data[i][j] in '0,1,2,3,4,5,6,7,8,9':
                t += data[i][j]
            elif data[i][j] == 'х':
                t += ','
        r.add(t)
        t = ''
    print(r)

get_tuple(p_p2)




# 7*xˆ2 
    # (7, 2)
# 9*x
    # (9, 1)
# 41
    # (41, 0)



# path = '/Users/andreyprusakov/Desktop/GB projects/python/polinom3.txt'
# f = open (path, 'w')
# f.writelines(s)
# f.close()
