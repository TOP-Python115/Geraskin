#Задача 122
# Поросячьей латынью» называют молодежный жаргонный язык, производный от английского. И  хотя корни этого новообразованного языка 
# неизвестны, упоминание о  нем есть как минимум в  двух документах, датированных XIX веком, а  это значит, что ему уже больше сотни лет. 
# Для перевода слова с английского на «поросячью латынь» нужно сделать следующее:
# если слово начинается с согласной буквы (включая y), то все буквы с начала слова и до первой гласной (за исключением y) переносятся 
# в конец слова и дополняются сочетанием букв ay. Например, слово computer будет преобразовано в omputercay, а слово think – в inkthay;
# если слово начинается с гласной буквы (не включая y), к концу слова просто добавляется way. К примеру, слово algorithm превратится 
# в algorithmway, а office – в officeway.
# Напишите программу, которая будет запрашивать у пользователя строку. После этого она должна переводить введенный текст на «поросячью 
# латынь» и выводить его на экран. Вы можете сделать допуск о том, что все слова пользователь будет вводить в нижнем регистре и разделять их 
# пробелами.


m = input()
m = m.lower().split()

def first_vowel(m):
    i = 0   
    while i < len(m):
        if m[i] in 'aeiou':
            return i
        i += 1
    return len(m) - 1
 
            
for i in range(len(m)):
    if m[i][0] in 'aeiou':
        m[i] = m[i] + 'way'
    else:
        m[i] = m[i][first_vowel(m[i]):]+m[i][:first_vowel(m[i])]+'ay'
        
print(*m)        
        
#Задача 123
#Нет решения
