#Упражнение 114
# Напишите программу, запрашивающую у пользователя целые числа, пока 
# он не оставит строку ввода пустой. После окончания ввода на экран должны быть выведены сначала все отрицательные числа, 
# которые были введены, затем нулевые и только после этого положительные. Внутри каждой 
# группы числа должны отображаться в той последовательности, в которой 
# были введены пользователем. Например, если он ввел следующие числа: 
# 3, -4, 1, 0, -1, 0 и -2, вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. 
# Каждое значение должно отображаться на новой строке.

l = []
while s := input():
    l += s.split()

l = [int(el) for el in l]

l1 = [el for el in l if el < 0]
l2 = [el for el in l if el == 0]
l3 = [el for el in l if el > 0]


print(*l1, sep = '\n')
print('---------------')
print(*l2, sep = '\n')
print('---------------')
print(*l3, sep = '\n')

# 4
# 6
# 0
# -4
# 3
# 2
# -6
# -5
# 4
# 0
# 1
# 3
# 5

# -4
# -6
# -5
# ---------------
# 0
# 0
# ---------------
# 4
# 6
# 3
# 2
# 4
# 1
# 3
# 5

