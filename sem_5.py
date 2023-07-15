# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# вариант 1

# lst = [3,2,1,4,5,4,5,2]
# min_elem = min(lst)
# max_elem = max(lst)
# new_lst = []
# print(lst)

# for elem in lst:
#     if elem == max_elem:
#         new_lst.append(min_elem)
#     # elif elem == min_elem:
#     #     new_lst.append(max_elem)
#     else:
#         new_lst.append(elem)
# print(new_lst) 

# вариант 2

# def aven(input_arr):
#     result_arr = []
#     minmin = min(input_arr)
#     maxmax = max(input_arr)
#     if minmin != maxmax:
#         for i in range(len(input_arr)):
#             if input_arr[i] == maxmax: 
#                 result_arr.append(minmin)
#             else: 
#                 result_arr.append(input_arr[i])
#     else: 
#         result_arr = input_arr
#     return result_arr

# def T33():
#     input_str = input('Введите массив: ')
#     input_arr = [int (x) for x in input_str.split()] 
#     print(aven(input_arr))

# T33()

# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# def is_simple (num):
#     for i in range (2, num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True

# a = int(input())
# print(is_simple(a))

