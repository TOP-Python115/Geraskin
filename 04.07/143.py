# Упражнение 143. Анаграммы
# Анаграммами называются слова, образованные путем взаимной перестановки букв. 
# В английском языке, например, анаграммами являются слова 
# «live» и «evil», а в русском – «выбор» и «обрыв». Напишите программу, которая 
# будет запрашивать у пользователя два слова, определять, являются 
# ли они анаграммами, и выводить на экран ответ.


s1, s2 = input('Введите первое слово для проверки\n').lower(), input('Введите второе слово для проверки\n').lower()
v1 = {c: s1.count(c) for c in s1}
v2 = {c: s2.count(c) for c in s2}
print (v1)
print (v2)
print('Слова являются анаграммами' if v1 == v2 else 'Слова не являются анаграммами')

# C:\Users\Admin\Documents\python\Python\Homework\0407>py.exe Python115_Geraskin_2022_0407_task143.py
# Введите первое слово для проверки
# live
# Введите второе слово для проверки
# evil
# Слова являются анаграммами

# C:\Users\Admin\Documents\python\Python\Homework\0407>py.exe Python115_Geraskin_2022_0407_task143.py
# Введите первое слово для проверки
# super
# Введите второе слово для проверки
# power
# Слова не являются анаграммами