"""
Задание 1
Пользователь вводит с клавиатуры строку. Проверьте является ли введенная строка палиндромом.
Палиндром — слово или текст, которое читается одинаково слева направо и справа налево.
Например, кок; А роза упала на лапу Азора; доход; А буду я у дуба.
"""


def reverse(text):
    return ''.join(reversed(text))


user_text = input("Введите текст, чтоб проверить является ли он палиндромом: ")
user_text = user_text.lower()
user_text = user_text.replace(" ", '')

if user_text == reverse(user_text):
    print("Палиндром!")
else:
    print("Не палиндром.")


"""
Задание 2
Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов. 
Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. 
Вывести на экран измененный текст.
"""

my_text = input("Введите текст: ")
my_text_temp = my_text.lower()
list_told = list(my_text.split())
list_new = list(my_text_temp.split())
count_words = None
word = []

while True:
    count_words = input("Введите кол-во зарезервированных слов: ")
    if count_words.isdigit():
        count_words = int(count_words)
        break
    else:
        print("Не число!")
        continue

for count in range(0, count_words):
    word_in_list = input(f"Введите зарезервированное слово №{count+1}: ")
    if word_in_list.isalpha():
        word.append(word_in_list)
    else:
        print("Не слово!")
        exit(1)

for i in range(len(list_new)):
    for j in word:
        if j in list_new[i]:
            list_told[i] = list_new[i].upper()
print(' '.join(list_told))


"""
Задание 3
Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный результат.
"""

example_text = input("Введите текст, чтоб посчитать в нем кол-во предложений: ")
count = example_text.count('. ') + example_text.count('! ') + example_text.count('? ') + 1
print(f"Кол-во предложений: {count}")

