# Найти сумму чисел списка стоящих на нечетной позиции
a = list('549i6984014901')
def sum_of (a):
    res = int(0)
    for i in range (1,len(a),2):
        if a[i].isnumeric(): res += int(a[i])
    return (res)
print(sum_of(a))

