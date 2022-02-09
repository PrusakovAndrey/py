# *******************
# def select (f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# print (data)
# res = select (int, data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x: (x, x**2), res)
# print (res)

# *******************
# li = [x for x in range (1,20)]
# li = list(map(lambda x: x+10,li))
# print (li)

# *******************
# data = map(int,'1 2 3 4 5'.split())
# for e in data:
#     print (e*10)

# *******************
# data = '1 2 3 5 8 15 23 38'.split()
# res = map (int, data)
# res = list(filter(lambda x: not x%2, res))
# # res = list(map(lambda x: (x, x**2), res))
# print (res)

# data = [x for x in range (10)]
# res = list(filter(lambda x: not x %2, data))
# print (res)

# *******************
# users = ['user1', 'user2', 'user3', 'user4']
# id = [1, 2, 3, 4]
# salary = [100,150,75]

# table = list(zip(users, id, salary))
# print (table)

# *******************
# out = list(enumerate(['user1', 'user2', 'user3', 'user4']))
# print (out)

# *******************
with open('/Users/andreyprusakov/Desktop/GB projects/python/file.txt') as data:
    print(data)
