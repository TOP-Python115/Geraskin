#Задание3
#Вводятся два целых числа не равных нулю. Напишите программу, которая проверяет делится ли первое число на второе нацело. 
#Программа выводит сообщение об этом, а также частное и остаток, если он есть.
#Для вывода используйте f-строку.

a1 = int(input(f"Введите первое лое число не равное нулю "))
a2 = int(input(f"Введите второе целое число не равное нулю "))
if (a1 % a2 == 0):
    print(f"Число {a1} делится на {a2} нацело")
    print(f"Частное: {int(a1/a2)}")
else:
    print(f"Число {a1} не делится на {a2} нацело")
    print(f"Частное: {int(a1/a2)}")
    print(f"Остаток: {int(a1%a2)}")
    
