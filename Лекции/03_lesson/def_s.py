def matrix (n,m):
    from random import randint
    a = [[randint(-100, 100) for j in range(n)] for i in range(m)]
    return (a)


print(matrix(4,4))
