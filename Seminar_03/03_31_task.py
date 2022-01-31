# Составить список простых множителей натурального числа N


n = 3276

def task31 (n):
    i = 2
    array = []
    while n != 1: 
        if n % i == 0:
            array.append(i) #3
            n = n / i
            i = 2
            print (n)
        else: 
            i += 1
            print (n)
    return (array)

print (task31 (n))

# def primfacs(n):
#     i = 2
#     primfac = []
#     while i * i <= n:
#         while n % i == 0:
#             primfac.append(i)
#             n = n / i
#         i = i + 1
#     if n > 1:
#         primfac.append(n)
#     return primfac
# print (primfacs (n))