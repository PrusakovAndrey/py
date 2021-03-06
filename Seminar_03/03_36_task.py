# Дан список чисел. Выделить среди них числа, удовлетворяющие условию: 
# следующее больше предыдущего. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

ls = [1, 5, 2, 3, 4, 6, 1, 7] #, 9, 8, 10]

# ch_indx = min(ls[0],ls[1],ls[2])
# res = [ch_indx]
# for i in range (2,len(ls)):
#     if ls[i-2]>ch_indx and ls[i-2]<max(ls[i-1], ls[i]):
#         res.append(ls[i-2])
#         ch_indx = ls[i-2]
#     if ls[i] == max(ls):
#         res.append(ls[i])
#         break
# print(res)


# решение от Натальи

def get_up2 (nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
#print(get_up2(ls))

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups
print(get_up(ls))