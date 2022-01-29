# Определить, присутствует ли в заданном списке строк, некоторое число 
a = 9
def file_to_list (path, a):
    data = open(path, 'r')
    indat = str()
    for d in data:
        indat +=(str(d))
    data.close()
    if indat.find(str(a)) != -1:
        return True
print(file_to_list('file1.txt',a))

