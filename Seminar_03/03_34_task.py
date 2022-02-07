# Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.



from re import X


path1 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom1.txt'
path2 = '/Users/andreyprusakov/Desktop/GB projects/python/polinom2.txt'

def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

print(reading(path1))
print(reading(path2))

s = '7*xˆ2 + 9*x + 41 = 0'
a = s.split('+')

# 7*xˆ2 
    # (7, 2)
# 9*x
    # (9, 1)
# 41
    # (41, 0)



path = '/Users/andreyprusakov/Desktop/GB projects/python/polinom3.txt'
f = open (path, 'w')
f.writelines(s)
f.close()
