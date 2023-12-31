# import math
#
# def all_divisors(number):
#     divisors = []
#     for i in range(1, int(math.sqrt(number)) + 1):
#         if number % i == 0:
#             divisors.append(i)
#             if i != number // i:
#                 divisors.append(number // i)
#     divisors.sort()
#     return divisors
#
# number1 = 23436
# number2 = 190187200
# number3 = 380457890232
#
# divisors1 = all_divisors(number1)
# divisors2 = all_divisors(number2)
# divisors3 = all_divisors(number3)
#
# print(divisors1)
# print(divisors2)
# print(divisors3)

#
# def three_args(var1, var2, var3):
#     res_dict = locals()
#     print('Аргументы: ', *(f'{key} = {value}' for key, value in res_dict.items() if value))
#
#
# three_args(1, None, 'asd')
#
# from string import punctuation
#
# text = '''Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.
# Напишите пожалуйста решение на Python'''
#
# tbl = str.maketrans('', '', punctuation)
# words = text.translate(tbl).lower().split()
# print(max(words, key=len))
# print(max(set(words), key=lambda x: words.count(x)))

# n, m = map(int, input().split())
# matrix = [[0] * m for _ in range(n)]
# dx, dy, x, y = 0, 1, 0, 0
#
# for i in range(1, n * m + 1):
#     matrix[x][y] = i
#     if matrix[(x + dx) % n][(y + dy) % m]:
#         dx, dy = dy, -dx
#     x += dx
#     y += dy
# for line in matrix:
#     print(*(f'{i:<3}' for i in line), sep='')

#
# n, m = (int(i) for i in input().split())
# spiral = []
# x, y, dx, dy, k = 0, 0, 1, 0, 1
# spiral = [[0] * n for _ in range(m)]
# for i in range(1, n * m + 1):
#     spiral[x][y] = i
#     nx, ny = x + dx, y + dy
#     if 0 <= nx < m and 0 <= ny < n and spiral[nx][ny] == 0:
#         x, y = nx, ny
#     else:
#         dx, dy = -dy, dx
#         x, y = x + dx, y + dy
# for i in range(n):
#     for j in range(m):
#         print(str(spiral[j][i]).ljust(3), end=' ')
#     print()