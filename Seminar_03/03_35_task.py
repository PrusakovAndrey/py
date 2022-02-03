# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

a = str('10 6 4 8 9 5')

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


