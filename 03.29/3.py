# Задание3
# На вход программе даётся строка, состоящая из слов, разделенных пробелами. 
# Напишите программу, которая подсчитывает количество слов в этой строке.
# Примечание: задачу можно решить в одну строку кода.

c = input(f'Введите текст для подсчета количества слов в нем \n')
print (f"{c.count(' ') + 1}")
