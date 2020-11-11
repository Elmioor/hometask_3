# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
# print("enter first integer")
# user_input_one = int(input())
# print("enter second integer")
# user_input_two = int(input())
#
#
# def funk_task_one(int_one, int_two):
#     devizion_result = None
#     if int_two == 0:
#         print("divide by zero exeption")
#     else:
#         devizion_result= int_one/int_two
#     return devizion_result
#
# print(funk_task_one(user_input_one,user_input_two))

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
# n="aaa"
# sn="bbb"
# by=1999
# dc="NY"
# em="a@b.c"
# ph="9999999"
#
# def funk_task_two(name="name", surname="surname", birthyear=1666, defaultcity="Moscow", email="some#@mail.org", phone="+76666666666"):
#     print(name, surname,birthyear,defaultcity,email,phone)
#
# funk_task_two()
#
# funk_task_two(n,sn,by,dc,em,ph)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
#
# """ values for possible input"""
# i1=4
# i2=5
# i3=6
#
#
#
# def my_funk(integ_one=1,integ_two=2,integ_three=3):
#
#     mas_one = [integ_one,integ_two,integ_three]
#     first_max=max(mas_one)
#     mas_one.remove(max(mas_one))
#     mas_two=mas_one
#
#     funk_result = first_max + max(mas_two)
#     return funk_result
#
# """calling funktion """
# print(my_funk(i1,i2,i3))

#my_funk(i1,i2,i3)

## 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
#

# x=None
# y=None
#
# x=2
# y=-3
#
# def my_funk_task_four_oneway(x,y):
#     first_solution = x ** y
#     print(first_solution)
#
# def my_funk_task_four_waytwo(x,y):
#     rez=1
#     for i in range(0, y, -1):
#         rez = rez*x
#         i= i-1
#
#     return 1/rez
#
# my_funk_task_four_oneway(x,y)
# print(my_funk_task_four_waytwo(x,y))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

# !!!!!!!!!!!!!!!!! В ступоре, покка не придумал, как доделать, из материалов лекции материалов не хватило
#
# print("enter data - using space bars  separates elements")
# string_to_parse_on = input()
# #print(string_to_parse_on)
# list_of_numbers = string_to_parse_on.split()
#
# adding_elems = 0
# sum_of_elems = 0
# for el in list_of_numbers:
#
#     if el == 'z'in list_of_numbers:
#         elem_to_pop = list_of_numbers.index('z')
#         i=0
#
#         while i < elem_to_pop:
#             sum_of_elems += int(list_of_numbers[i])
#
#             i +=1
#
#     else:
#         sum_of_elems += int(el)
#
#
# print(sum_of_elems)

Exit = False
summ = 0

while not Exit:
    new_line = input()
    elements = new_line.split(' ')
    for e in elements:
        if e.strip() == 'z':
            print(summ)
            Exit = True
        elif e.strip().isdigit():
            summ += int(e)
            print(summ)



# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# print("please enter a string")
# user_input = input()
#
# def int_funk_task_six_one_word(string_word):
#     splited_str = string_word.split()
#     i=0
#     while i < len(splited_str):
#         print(splited_str[i].capitalize(), end=' ')
#         i +=1
#
# int_funk_task_six_one_word(user_input)
