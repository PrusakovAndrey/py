#Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def tsk16 (f):
    a = 1
    res = 0
    for e in range (1,f+1):
        res += (1+1/e) ** e
        print (res)
    return(res)

print(tsk16(4))