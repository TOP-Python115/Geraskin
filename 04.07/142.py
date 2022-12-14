# Упражнение 142. Уникальные символы
# (Решено. 16 строк)
# Напишите программу, определяющую и выводящую на экран количество 
# уникальных символов во введенной пользователем строке. Например, 
# в строке Hello, World! содержится десять уникальных символов, а в строке 
# zzz – один. Используйте словарь или набор для решения этой задачи.

text = input('Введите фразу для определния количества уникальных символов\n').lower()
p = set()
for i in text:
    p.add(i)
print(len(p))

# C:\Users\Admin\Documents\python\Python\Homework\0407>py.exe Python115_Geraskin_2022_0407.py
# Введите фразу для определния количества уникальных символов
# zzz
# 1

# C:\Users\Admin\Documents\python\Python\Homework\0407>py.exe Python115_Geraskin_2022_0407.py
# Введите фразу для определния количества уникальных символов
# Hello, world!
# 10


# Упражнение 143. Анаграммы
# Анаграммами называются слова, образованные путем взаимной перестановки букв. 
# В английском языке, например, анаграммами являются слова 
# «live» и «evil», а в русском – «выбор» и «обрыв». Напишите программу, которая 
# будет запрашивать у пользователя два слова, определять, являются 
# ли они анаграммами, и выводить на экран ответ.

# Упражнение 144. Снова анаграммы
# Понятие анаграмм не ограничивается словами, а может быть расширено 
# до целых предложений. Например, строки «William Shakespeare» и «I am 
# a weakish speller» являются полными анаграммами, если игнорировать 
# пробелы и заглавные буквы.
# Расширьте свою программу из упражнения 143, добавив возможность 
# проверки на анаграммы целых фраз. При анализе не обращайте внимания 
# на знаки препинания, заглавные буквы и пробелы.

