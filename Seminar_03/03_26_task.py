# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
а

def fibo(n):
    if n in (1,2):
        return 1
    return (fibo(n-1) + fibo(n-2))

def print_fib (a):
    list = []
    for e in range (1,a+1):
        list.append(fibo(e))
    return list
print (print_fib(6))