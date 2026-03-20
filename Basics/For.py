#1
# s = 0
# for x in range(100):
#     s += x
# print(f"Sum = {s}")

#2
# s = 0
# for x in range(1, 52):
#     if x % 2 == 1:
#         s += x
# print(s)

#3
# s = 0
# for x in range(200, 301):
#     if x % 2 == 0:
#         s += x
# print(s)

#4
# count = 0
# for i in range(0,1001):
#     if i % 3 == 0:
#         count += 1
# print(count)

#5
# count_1 = 0
# count_2 = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         count_2 += 1
#     else:
#         count_1 += 1
# print(count_1, count_2)

#6
# n = int(input('Enter any n: '))
# k = int(input('Enter any k: '))
# s = 0
# for x in range(n, k + 1):
#     if x % 2 == 0:
#         s += x
# print(s)

#7
# n = int(input('Enter any n: '))
# k = int(input('Enter any k: '))
# for x in range(k+1):
#     x = n ** k
# print(x)

#8
# f = 1
# for x in range(1,8):
#     f = f * x
# print(f'x! = {f}')

#9
# total_1 = 200
# days = 10
# daily = 3
# total_2 = 0
# for x in range(1, days + 1):
#     total_2 += daily
#     daily += 3
# print(total_1 - total_2)

#10
# l = int(input('Enter any number of lines: '))
# s = '*'
# for x in range(l + 1):
#     print(s * x)

#11
# l = int(input('Enter any number of steps: '))
# s = '#'
# for x in range(1, l + 1):
#     print(s.rjust(x))

#12
# l = int(input('Enter any number of lines: '))
# s = '*'
# w = 2 * l - 1
# for x in range(l + 1):
#     b = 2 * x - 1
#     f = s * b
#     print(f.center(w))

#1s
# s = 'Hello'
# for i in range(len(s)):
#     print(i, s[i])
#
#2s
# s = 'Summer'
# for i in range(len(s)):
#     print(f"{s[i]} - {i}")

#3s
# s = "The Phantom of the Opera"
# count = 0
# for letter in s:
#     if letter.isupper():
#         count += 1
# print(count)

#4s
# s = 'My name is Issak'
# count = 0
# for letter in s:
#     if letter.lower() in ['a','e','i','o','u'] or letter.upper() in ['A','E','I','O','U']:
#         count += 1
# print(count)

#5s
# s = 'Unique'
# res = ''
# for i in s:
#     res = res + i * 2
# print(res)

#6s
# s = input('Enter any string: ')
# res = ''
# for i in s:
#     res = res + i + ' '
# print(res)

#7s
# s = '1Grape, 6Potatos, 3apples'
# res = ''
# for i in s:
#     if i.isdigit():
#         res = res + i + ' '
#     else:
#         res = res + i
# print(res)

#8s
# s = input('Enter any string: ')
# res = ''
# for letter in s:
#     if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
#         res = res + letter.upper()
#     else:
#         res = res + letter
# print(res)

#9s
# s = input('Enter any string: ')
# res = ''
# for letter in s:
#     if letter in ['a', 'e', 'i', 'o', 'u'] or letter in ['A','E','I','O','U']:
#         res = res + '*'
#     else:
#         res = res + letter
# print(res)

# s = input('Enter any string: ')
# vowels = 'aeiouAEIOU'
# for letter in vowels:
#     s = s.replace(letter, '*')
# print(s)

#10s
# s = input('Enter any string: ')
# vowels = 'aeiouAEIOU'
# for letter in vowels:
#     s = s.replace(letter, '')
# print(s)

#11s
# s = 'option'
# res1 = ''
# res2 = ''
# for i, letter in enumerate(s):
#     if i % 2 == 0:
#         res1 = res1 + letter
#     else:
#         res2 = res2 + letter
# print(res1)
# print(res2)

#12s
# s = 'LetS Go'
# for i in s:
#     if i.lower() > i.upper():
#         s = s.lower()
#     else:
#         s = s.upper()
# print(s)

