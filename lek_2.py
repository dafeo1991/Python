# создание и вывод списков

# list_1 = ['a', 's', 'd', 'f']
# list_2 = list([1, 2, 3])
# list_3 = [1, 2, 3, 8]
# print(list_1)
# print(list_2)
# print(*list_3)

# for i in list_3:
#     print(i)

# количество эл в списке

# print(len(list_1))

# обратится к элементу списка, если индекс с - то с конца

# print(list_1[3])
# print(list_1[-3])

# добавить эл в список

# print(list_1)
# list_1.append(5)
# print(list_1)

# наполняем список

# list_1= []
# print(list_1)

# for i in range(10):
#     list_1.append(i)
#     print(list_1)

# удаление последнего элемента

# list_1 = [12, 7, 1, 21, 0]
# print(list_1)
# print(list_1.pop())
# print(list_1)

# удаление конкретного элемента

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0))
# print(list_1)

# добавление эл на нужную позицию

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1)

# кортежи

# t = ()
# print(type(t))

# t = (1, 5, 3, )
# print(type(t))

# преобразовать список в кортеж

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v)
# print(v)
# print(type(v))

# разъеденить кортеж на переменные, множественное присваивание

# a, b, c = v

# print(a, b, c) # распаковка кортежа

# вывод по индексам

# t = (1, 2, 3, 5)

# for i in range(len(t)):
#     print(t[i])

# словари

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d)

# print(d['q'])

# удаление элемента

# d = {}
# d = {1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 6}
# print(d)
# del d[5]
# print(d)

# for item in d:
#     print(item)
#     print('{} : {}'.format(item, d[item]))

# print(d.items()) # выводится список где каждый элемент кортеж из 2 значений: клич и значение

# for (k, v) in d.items():
#     print(k, v) # k - ключ v - значение

# множества

# collor = {'red', 'green', 'blue'}
# print(collor)

# collor.add('red')  # если добавляем то что есть то оно не добавится
# print(collor)

# collor.add('grey')   # добавить
# print(collor)

# collor.remove('red')   # удалить, если уже удален то будет ошибка
# print(collor)

# collor.discard('red')   # удалить если уже удален то не будет ошибка, просто пропустит
# print(collor)

# collor.discard('green')   # удалить
# print(collor)

# collor.clear()   # удалить все элементы 
# print(collor)


# операции со множествами

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy() # скопировать множество
# print(c)
# u = a.union(b) # объеденить
# print(u)
# i = a.intersection(b) # пересечение (эл которые есть  в обоих множествах)
# dl = a.difference(b) # разность между множествами
# dr = b.difference(a)
# print(dl, dr)
# q = a.union(b).difference(a.intersection(b))
# print(q)

# замороженные множества

# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

# доступ к элементам списка

# list_1 = [1, 2, 5, [1, 2,9]]

# print(list_1[2])

# print()

# for elem in list_1:
#     print(elem)

# print()

# for i in range (4):
#     print(list_1[i])

# заполнить список

# list_1 = [0] * 3

# удалить несколько элементов

list_1 = ['a', 's', 'd', 'f']
print(list_1)

# for i in range(2):
#     the_last = list_1.pop(1)
# print(list_1)

# срезы

list_2 = list_1[2:]
print(list_2)