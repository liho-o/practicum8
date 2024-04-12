"""
Напишите программу вычисляющую средний доход жителей города Н.
Программа получает на вход месячный доход каждого гражданина этого города.
Каждое значение вводится в отдельной строке. Количество жителей не известно.
Окончанием ввода данных является значение 0.
"""


def average(list_income):
    total = 0
    for i in list_income:
        total += i
    return total / len(list_income)


def checking_income():
    total = []
    while True:
        score = int(input())
        if score == 0:
            total.sort()
            return average(total)
        else:
            total.append(score)


print(checking_income())
