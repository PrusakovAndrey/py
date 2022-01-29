# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def high (f):
    t = 1
    res = list()
    #[(res.append(e*t)) for e in range (1,f+1)]
    for e in range (1,f+1): 
        t = e*t
        res.append(t)
    return res

print (high(6))