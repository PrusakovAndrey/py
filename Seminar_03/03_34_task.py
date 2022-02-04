#Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
a

path1 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom1.txt'
path2 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom2.txt'

def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

print (reading(path1))
print (reading(path2))
