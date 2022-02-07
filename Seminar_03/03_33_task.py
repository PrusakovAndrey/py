# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 3
m1 = randint(0, 100)
m2 = randint(0, 100)
m3 = randint(0, 100)

def polinom_2_file (k,m1, m2, m3):
    s1 = ('{}xˆ{} + {}*x + {}'.format (m1, k, m2, m3))
    path = '/Users/andreyprusakov/Desktop/GB projects/python/Seminar_03/33_task.txt'
    f = open (path, 'w')
    f.writelines(s1)
    f.close()
polinom_2_file(k,m1,m2,m3)