#Задание1
#На вход программе подаётся два натуральных числа n и m, каждое на отдельной строке. 
#Напишите программу, которая печатает прямоугольник из символов ‘*’ размерами n×m.
n = int(input(f"Введите длинну стороны прямоугольника n "))
m = int(input(f"Введите длинну стороны прямоугольника m "))

for i in range (0, n):
    print ('*'*m)