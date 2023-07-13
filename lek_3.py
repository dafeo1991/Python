# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
# sum_numbers(5)

# возвращает значение

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
#     print('stop')

# print(sum_numbers(5))

# передаем неограниченное кол-во аргументов

# def sum_str(*args):
#     res = 0
#     #res = ''
#     for i in args:
#         res += i
#     return res
# #print(sum_str('q', 'w', 'e', 'r', 't', 'y'))
# print(sum_str(1, 8, 9))

# импортируем модуль

# import modul

# print(modul.max1(5, 9))

# импортируем функцию

# from modul import max1

# print(max1(5, 9))

# импортировать модуль под другим именем

# import modul as n1

# print(n1.max1(5, 9))

# рекурсия, числа фибоначи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []

# for i in range(1, 15):
#     list_1.append(fib(i))

# print(list_1)

# Алгоритмы сортировки от большего к меньшему
# быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10, 5, 2]))

# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [3,8,78,95,1,-2,5,85,104.75,12,0]
merge_sort(list_1)
print(list_1)
