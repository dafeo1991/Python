# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]


# a = [1, 1, 2, 0, -1, 3, 4, 4]

# new = []

# for el in a:
#     if el not in new:
#         new.append(el)
# print(len(new), new)

# через множества способ 2

# a2 = set(a)
# count = len(a2)
# print(count)


# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3

b = [1, 2, 3, 4, 5]
# print(b) 

k = 3

# for i in range(k):
#     last = b.pop()
#     b.insert(0, last)
# print(b) 

# через срез

b2 = b[k:] + b[:k]

print(b, b2)

# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# c = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(c)):
#     if c[i] > c[i - 1]:
#         count += 1
# print(count)







