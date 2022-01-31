# Пользователь задаёт две строки. Определить количество 
# вхождений одной строки в другой.
atext = input(str('-->>'))
btext = input(str('-->>'))

from gettext import find

# def matching (atext, btext):
#     count = set([])
#     c = ''
#     if (atext.find(btext) == -1 and btext.find(atext) == -1): return False
#     elif btext.find(atext) == -1:
#         for i in range(len(atext)): 
#             c = atext.find(btext, i,len(atext))
#             count.add(c)
#         return len(count)-1
#     else:
#         for i in range(len(btext)): 
#             c = btext.find(atext, i,len(btext)) 
#             count.add(c)
#         return len(count)-1

# print(matching(atext, btext))

def including (a,b):
    if a.count(b) > 0:
        return a.count(b)
    elif b.count(a) > 0:
        return b.count(a)
    return False

print(including(atext, btext))