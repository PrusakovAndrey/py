# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным 
# значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5, 10.01]
def task24 (a):
    bl_list = []
    for e in range (0,len(a)):
        temp = round((a[e]-int(a[e])),2)
        if temp != 0:
            bl_list.append(temp)
    return (max(bl_list)-min(bl_list))
print (task24(a))
