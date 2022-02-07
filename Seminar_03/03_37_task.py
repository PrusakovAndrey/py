# Дан список чисел. Создать список в который попадают числа, 
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

ls = [5, 2, 3, 4, 6, 1, 7] #, 9, 8, 10]

def trend (str):
    ch_indx = min(str[0],str[1],str[2])
    res = [ch_indx]
    for i in range (2,len(str)):
        if str[i-2]>ch_indx and str[i-2]<max(str[i-1], str[i]):
            res.append(str[i-2])
            ch_indx = str[i-2]
        if str[i] == max(str):
            res.append(str[i])
            break
    return res
print(trend(ls))