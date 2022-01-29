# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

from datetime import datetime

def rand ():
    a = datetime.now()
    return a.microsecond%10

print(rand())