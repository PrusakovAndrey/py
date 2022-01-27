# Пользователь задаёт две строки. Определить количество 
# вхождений одной строки в другой.
a = input(str('-->>'))
b = input(str('-->>'))

def str_to_set (f):
    res = set([])
    for e in range (0,len(f)):
        res.add(f[e])
    return (res)

c = (str_to_set(a)).intersection(str_to_set(b))
print(len(c))
