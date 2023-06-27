# # типы переменных

# b = 7
# a = 1.89
# s = None
# n = 'as""df'

# # вывести в консоль класс переменной

# print(type(n))

# #вывести в консоль несколько переменных

# print(f"{a} - {s} - {n}")
# print("{} - {} - {}" .format(a,s,n))

# # ввод данных в консоли

# print("введите первую строку")
# o = input()
# print(o)

# # приведение типов данных

# print("Введите первое число ")
# a1 = input()
# print("Введите второе число ")
# a2 = input()

# print(a1, '+', a2, '=', a1 + a2)

# b1 = 5.89
# print(b1)
# print(type(b1))

# b1 = int(b1)
# print(b1) 
# print(type(b1))

# b1 = str(b1)
# print(b1) 
# print(type(b1))

# b1 = bool(b1)
# print(b1) 
# print(type(b1))


# print("Введите первое число ")
# a1 = int(input())
# a2 = int(input("Введите второе число "))
# print(a1, '+', a2, '=', a1 + a2)

# округление чисел

# a = 5.456
# b = 3.28

# print(round(a*b, 3))

# логические операции

# a = 1 > 4
# print(a)

# b = 1 < 4 and 5 > 2
# print(b)

# c = 1 == 2
# print(c)

# d = 1 != 2
# print(d)

# e = 'asd'
# f = 'asd'
# print(e == f)

# g = 1 < 3 < 5 < 10
# print(g)

# управляющие конструкции if elif else

# name = input("Введите имя ")
# if name == "Маша":
#     print("Ура, это же МАША!")
# elif name == "Марина":
#     print("Я так ждала Вас, Марина!")
# elif name == "Ильнар":
#     print("Ильнар - топ!")
# else :
#     print("Привет,", name) 

# управляющие конструкции while

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print("Пожалуй хватит")
# print (i)

# метод флага

# n = int(input()) 
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i = 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введеное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# цикл for и вложенные циклы

# a = 'qwerty'

# print(a[0])

# for i in a:
#     print(i) 

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# функции

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # функция len показывает размер строки
# print('ещё' in text) # проверяет есть ли данное слово в переменной
# print(text.lower()) # все буквы приводит к нижнему регистру
# print(text.upper()) # все буквы приводит к верхнему регистру
# print(text.replace('ещё', 'ЕЩЁ' )) # меняет указанный элем, сначала пишем что меняем потом на какой меняем

text = 'съешь ещё этих мягких французских булок'
# print(text[0])
# print(text[1])
# print(text[len(text) - 1])
# print(text[-1]) # если индекс с - то элем выводяца с конца строки
# print(text[-5])


print(text[:]) # выводится все
print(text[:2]) # выводится элементы с 0 по 2 не включительно
print(text[len(text) - 2:]) # элементы с конца
print(text[2:9]) # со 2 по 9 элем
print(text[6:-18]) # начинаем с 6 и идем в обратную сторону с конца
print(text[0:len(text):6]) # от 0 до конца строки с шагом 6, каждый 6 элемент
print(text[::6]) # то же самое

text = text[2:9] + text[-5] + text[:2]
print(text)
