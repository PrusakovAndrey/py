#Реализовать алгоритм перемешивания списка. 
from random import randint
l = list('a1b3c5d7e9f')
print(l)

def mix (x):
    for i in range (len(x)-1):
        number = x[i] # a , 
        index = randint(i+1, len(x)-1) # index = j from 1 to 10
        x[i] = x[index] # x0 now is any from next array
        x[index] = number # x any is a now
    return (x)

print(mix(l))


