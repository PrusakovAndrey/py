# Строка содержит набор чисел. Показать большее и меньшее число

a = str('12 24 789 1 7')

def max_min (a):
    b = []
    temp = str()
    for i in range (0,len(a)):
        if a[i] != ' ':
            temp += str(a[i])
        else: 
            b.append(temp)
            temp = str()
    return [max(b), min(b)]

print (max_min(a))


