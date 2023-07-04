# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# через список

# string = 'a a a b c a a d c d d'.split()
# print(string)

# answer = ''
# new_list = []

# for elem in string:
#     if elem in new_list:
#         answer += elem + '_' + str(new_list.count(elem)) + ' '
#     else:
#         answer += elem + ' '
#     new_list.append(elem)
# print(answer)

# через словарь

# from time import time
# from sys import getsizeof


# start = time()

# string = 'a a a b c a a d c d d'.split()
# print(string)

# answer = ''
# my_dict = {}

# for elem in string:
#     if elem in my_dict:
#         answer += elem + '_' + str(my_dict[elem]) + ' '
#         my_dict[elem] += 1
#     else:
#         answer += elem + ' '
#         my_dict[elem] = 1
# print(answer)
# print(my_dict)

# finish = time()
# print(finish - start)
# print(getsizeof(my_dict))
# print(getsizeof(answer))

# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

st = "shells sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the hells are sea shore shells"
words = st.split()
my_dict = {}
for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

values = my_dict.values()
max_value = max(values)
print(my_dict)
print(max_value)

print(words)
print(len(words))
print(len(set(words)))

for key, value in my_dict.items():
    if value == max_value:
        print(key, value)