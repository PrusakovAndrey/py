# Дан список чисел. Выделить среди них числа, удовлетворяющие условию: 
# следующее больше предыдущего. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

ls = [1, 5, 2, 3, 4, 6, 1, 7]

uniq = list(set(ls))

#print(uniq)

for j in range (0,len(uniq)):
    list = []
    ch_indx = uniq[j]
    print (ch_indx)
    for i in range (1,len(ls)):
        if(ls[i]>ch_indx):
            list.append(ls[i])
            ch_indx = ls[i]
    print(list)