# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
from itertools import count

a = [1, 2, 3, 5, 1, 5, 3, 10]
def uniq (str):
    res = []
    for i in range (len(str)):
        if str.count(str[i]) == 1:
            res.append(str[i])
    return res
print(uniq(a))