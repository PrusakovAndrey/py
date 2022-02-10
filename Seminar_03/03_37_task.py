# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

ls = [1, 2, 13, 6, 2, 4, 6, 1, 7, 9, 8, 10]

# def trend (a):
#     f = [0] * len(a)
#     prev = [-1] * len(a)
#     for i in range (len(a)):
#         m = 0
#         for j in range (i):
#             if a[j] < a[i] and f[j] >= m:
#                 m = f[j]
#                 prev[i] = j
#             f[i] = m + 1
#     ans = []
#     i = f.index(max(f))
#     ans.append(a[i])
#     while prev[i] != -1:
#         i = prev[i]
#         ans.append(a[i])
#     return ans [::-1]
# print(trend(ls))

# def trend (a):
#     f = [0] * len(a)
#     for i in range (len(a)):
#         m = 0
#         for j in range (i):
#             if a[j] < a[i] and f[j] >= m:
#                 m = f[j]
#             f[i] = m + 1
#     ans = []
#     i = f.index(max(f))
#     ans.append(a[i])
#     while f[i] > 1:
#          #ищем a[j]:a[j] < a[i] and f[j] == f[i] - 1
#          j = i - 1
#          while (a[j] >= a[i] or f[j] != f[i] - 1): #  пока не нашли 
#             j -=1
#          ans.append(a[j])
#          i = j
#     return ans [::-1]
# print(trend(ls))

