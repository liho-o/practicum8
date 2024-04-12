"""
Доработайте Задание 1. Напишите программу, которая определяет количество друзей.
"""

def checking_score():
    total = []
    while True:
        score = int(input())
        if score == -1:
            total.sort()
            return len(total)
        else:
            total.append(score)


print(checking_score())
