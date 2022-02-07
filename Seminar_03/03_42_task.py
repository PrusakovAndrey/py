# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах


path = '/Users/andreyprusakov/Desktop/GB projects/python/Seminar_03/42_coded.txt'
def reading (path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

a = (reading(path))
print(a)
def cortej (code):
    for i in range (0, len(code)):
        if code[i] == char:

        else:
            

def run_length_encoding(seq):
    compressed = []
    count = 1
    char = seq[0]
    for i in range(1,len(seq)):
        if seq[i] == char:
            count = count + 1
        else :
            compressed.append([char,count])
            char = seq[i]
            count = 1
    compressed.append([char,count])
    return compressed
