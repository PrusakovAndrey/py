#Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.



path1 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom1.txt'
path2 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom2.txt'

def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

s = '7 * xˆ2 + 5*x + ax + 41 = 0'

path = '/Users/andreyprusakov/Desktop/GB projects/python/polinom3.txt'
f = open (path, 'w')
f.writelines(s)
f.close()
