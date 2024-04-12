"""
Напишите программу, которая выводит в порядке возрастания все простые числа не превышающие N.
Число N вводится с клавиатуры. Программа не должна делать лишних проверок.
"""


def simple_check(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


N = int(input())

for num in range(2, N + 1):
    if simple_check(num):
        print(num)
