# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = input("st:")
# res = ''
# for ch in st:
#     if ch.isdigit():
#         res += ch
# res = ','.join(res)
# print(res)

##################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

#
#
text = input()

for item in text:
    if item.isdigit():
        print(item,end='')
    elif item == ' ':
        print(',',end='')
    else:
        delete = text.replace(item,'')




# #################################################################################
#
# list comprehension
#
# 1)есть строка:
greeting = 'Hello, world'
# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# list = []
# for i in greeting:
#    reg = i.upper()
#    list.append(reg)
#
# print(splitGreeting)
# print(list)
# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
#
# list = [pow(item, 2) for item in range(50) if item//2 != 0 or item ==0]
# print(list)

# item = 0

# while item < 50:
#    if item//2 != 0 or item == 0:
#       num = pow(item, 2)
#       list.append(num)
#    item += 1
#
# print(list)
# function
#
# - створити функцію яка виводить ліст
# list = [1, 2, 43, 5, 46, 5, 77, 68, 897, 987, 654, 5, 3425]
#
# def printList(l):
#     print(l)
#
# printList(list)


# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def findMinNumber(a, b, c):
#    minNumber = min(a, b, c)
#    print(minNumber)
#    return minNumber
#
#
#
# findMinNumber(121233, -323, -32)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def findMaxNumber(number1, number2, number3):
#     maxNumber = max(number1, number2, number3)
#     print(maxNumber)
#     return maxNumber
#
# findMaxNumber(24, -344, 43)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def func(*args):
#    maxNumber = max(args)
#    minNumber = min(args)
#    print(maxNumber)
#
#    return minNumber
#
# func(123, 12, 312, 4, 4, 324, 23)

# - створити функцію яка виводить ліст
# list = [1, 2, 43, 5, 46, 5, 77, 68, 897, 987, 654, 5, 3425]
#
# def printList(l):
#     print(l)
#
# printList(list)

# - створити функцію яка повертає найбільше число з ліста
#
# def returnMaxNumber(l):
#    key = 0
#    maxNumber = l[0]
#    for i in l:
#       if i > maxNumber:
#          maxNumber = l[key]
#       key += 1

#    return maxNumber
#
# returnMaxNumber([2,4,325,346,457,56,8,67,98,56, 76,523,4])

# - створити функцію яка повертає найменьше число з ліста

# def returnMinNumber(l):
#    key = 0
#    minNumber = l[0]
#    for i in l:
#       if i < minNumber:
#          minNumber = l[key]
#       key += 1
#
#    return minNumber
#
# returnMinNumber([2,4,325,346,457,56,8,0,67,98,56,-12, 76,523,4])

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def returnSumList(list):
#
#    sumList = 0
#
#    for item in list:
#       sumList += item
#
#    return sumList
#
#
# returnSumList([1, 23, 4, 1, 1])
# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def returnAvg(l):

#    sumAllNumbers = 0
#
#    for item in l:
#       sumAllNumbers += item
#
#    avg = sumAllNumbers / len(l)
#
#    return avg
#
# returnAvg([2,3,4,5])

# decorators
# - є функція:

#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
# def decor(func):
#     def wrap():
#         return func().replace('_', ' ')
#     return wrap
#
# @decor
# def pr():
#    return 'Hello_boss_!!!'
