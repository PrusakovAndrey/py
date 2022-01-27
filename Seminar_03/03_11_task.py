# Для натурального N создать множество: -3, 9, -27, 81 и т.д.

def variety (f):
    res = [-3]
    a = -3
    for i in range (1,f):
        a = a*-3
        res.append(a) 
    return (res)
print(variety(7))