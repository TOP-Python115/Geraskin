#Задание3
#На вход программе подаётся натуральное число n, а затем n целых чисел, 
#каждое на отдельной строке. Напишите программу, которая подсчитывает сумму 
#введённых положительных чисел.

n = int(input(f"Укажите число натуральных чисел для подсчета суммы положительных среди них "))
s = 0
for i in range (0, n):
    i = int(input())
    if i > 0:
        s = s + i 
print(s)
