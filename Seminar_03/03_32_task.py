# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

a = [1,4,1,5,9,2,6,5,3,5,8,9,7,9]

def uniq (a):
    b = []
    for i in range (len(a)):
        if a[i] not in b:
            b.append(a[i])
    return b
print (uniq(a))