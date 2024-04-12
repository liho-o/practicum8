"""
Напишите программу, которая выводит в порядке возрастания все совершенные числа не превышающие N.
Число N вводится с клавиатуры. Используйте циклы for.
"""


def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num

N = int(input("N: "))

for num in range(2, N + 1):
    if perfect_number(num):
        print(num)
