# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
import math

a = [2,3,4,5,6,7,0]
def task23 (a):
    res = []
    for i in range (0,int(math.ceil(len(a)/2))):
        res.append(a[i] * a[len(a)-(i+1)])
    return res
print (task23(a))