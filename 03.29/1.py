# Задание1
# Программа на вход получает строку содержащую адрес электронной 
# почты. Программа должна определить, является ли введённый пользователем 
# адрес корректным, и вывести соответствующее сообщение.
# Примечение: в корректном e-mail обязательно есть символ ‘@’, а после 
# него символ ‘.’


c = input('Введите адрес электроной почты ')

if c.find('@') == -1 or c.find('.') == -1 or c.find('@') > c.find('.') or c.find('@') == 0:
    print('Неверно')
else:
    print('Верно')
