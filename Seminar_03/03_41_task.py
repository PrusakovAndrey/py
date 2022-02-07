# Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

data = '2+2*3/2+1*3'
# mul = '*'
# mul_ls = []
# pl = '+'
# pl_ls = []
# mi = '-'
# mi_ls = []
# de = '/'
# de_ls = []
# print(data)
# for i in range (len(data)):
#     if data[i] == mul: mul_ls.append(i)
#     elif data[i] == pl: pl_ls.append(i)
#     elif data[i] == mi: mi_ls.append(i)
#     elif data[i] == de: de_ls.append(i)

# print (mul_ls)
# print (pl_ls)
# print (mi_ls)
# print (de_ls)

print(eval(data))