#Задание1
#Напишите программу, которая определяет, является число чётным или нечётным.
a = int(input(f"Введите число для проверки на четность "))
if a == 0:
    print(f"Число {a} не является четным/нечетным числом")
elif (a % 2) == 1:
   print(f"Число {a} является нечетным ")
else:
   print(f"Число {a} является четным ")
