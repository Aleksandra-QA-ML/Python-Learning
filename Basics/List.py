#простые списки
#1
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lst)
# print(len(lst))

#2
# lst = [38, 99, 157, 123, 297, 564, 1098]
# i1 = lst[0]
# i2 = lst[-1]
# print(i1 + i2)

#циклы for
#1
# lst = [-3, 0, 99, 5.4, 105]
# s = 0
# for i in lst:
#     s += i
# print(s)

#2
# lst = [-4, 56, 99, 133, 1568]
# s = 0
# for i in lst:
#     if i % 2 == 0:
#         s += i
# print(s)

#3
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# mlt = 1
# for i, el in enumerate(lst):
#     if i % 2 == 1:
#         mlt *= el
# print(mlt)

#4
# lst = [34, 99, -8, 67, 135, 73]
# s = 0
# for i in lst:
#     s += i
# if len(lst) > 0:
#     mdl = s/len(lst)
# print(mdl)

#5
# lst = [-23, 87, -100, 99, 45, 78, -149]
# count = 0
# for i in lst:
#     if i < 0:
#         count += 1
# print(count)

#6
# lst = [0, 5, 8, 15, 68, 100, 345]
# count = 0
# for i in lst:
#     if i % 5 == 0:
#         count += 1
# print(count)

#7
# lst = [-23, 87, -100, 99, 45, 78, -149, 388, 599, 1024]
# count = 0
# for i in lst:
#     if i % 2 == 0 and i > 0:
#         count += 1
# print(count)

#8
# arr = ["apple", "appricot", "pineapple", "banana", "grape", "plum"]
# count = 0
# for i in arr:
#     if len(i) == 5:
#         count += 1
# print(count)

#9
# arr = ["apple", "appricot", "pineapple", "banana", "grape", "orange"]
# voiels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for i in arr:
#     if i[0] in voiels:
#         count += 1
# print(count)

#10
# arr = ["apple", "appricot", "pineapple", "banana", "grape", "plum", "kiwi"]
# count = 0
# for i, el in enumerate(arr):
#     if 'a' in el:
#         count += 1
# print(count)

#create lists
#1
# lst = []
# for i in range(10):
#     lst.append(i*0)
# print(lst)

#2
# lst = []
# for i in range(1, 11):
#     lst.append(i)
# print(lst)

#3
# lst = []
# for el in range(0, 20,2):
#         lst.append(el)
# print(lst)

#4
# lst = []
# for i in range(20):
#     if i % 2 == 1:
#         lst.append(i)
# print(lst)

#5
# lst = []
# for i in range(10):
#     if i >= 0:
#         lst.append(2 ** i)
# print(lst)

#6
# str = 'August is the 7th month of the year'
# new_str = str.split()
# voiels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# lst = []
# for i, el in enumerate(new_str):
#     if el[0] in voiels:
#         lst.append(el)
# print(lst)

#7
# arr = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# lst = []
# for i in arr:
#     lst.append((32 + (i * 9/5)))
# print(lst)

#8
# lst = [0, 1]
# for i in range(8):
#     fib = lst[-1] + lst[-2]
#     lst.append(fib)
# print(lst)

#change_append_insert

#1
# lst = [0, 1, 3, 56, 98]
# new_lst = []
# for i in lst:
#     new_lst.append(i * -1)
# print(new_lst)

#2
# lst = [0, 1, 3, 56, 98, 156, 278]
# for i, el in enumerate(lst):
#     if el % 2 == 0:
#         lst[i] = 0
#     else:
#         lst[i] = 1
# print(lst)

#3
# lst = [0, 1, 3, 56, 98, 156, 278]
# for i, el in enumerate(lst):
#     if i % 2 == 0:
#         lst[i] = el ** 2
#     else:
#         lst[i] = el ** 3
# print(lst)

#4
# lst = [0, "Hello", 1, "7", 3, "9th", 98, "Ms. Anderson", 278]
# new_lst = []
# for i, el in enumerate(lst):
#     if type(el) is int or type(el) is float:
#         new_lst.append(el)
# print(new_lst)

#5
# lst = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
# voiels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# new_lst = []
# for i, el in enumerate(lst):
#     if  el[0] in voiels:
#         new_lst.append(el)
# print(new_lst)

#6
# lst = [0, 1, 3, 56, 98, 156, 278]
# new_lst = []
# for el in lst:
#     if type(el) is int:
#         new_lst.append(el * 2)
# print(new_lst)

#7
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# new_lst = []
# for el in lst:
#     absolut = abs(el)
#     string = str(absolut)
#     if len(string) % 2 == 0:
#         new_lst.append(el)
# print(new_lst)

#8
# lst = [0, 1, 3, 56, 25, 49, 81, 98, 156, 278]
# new_lst = []
# for el in lst:
#     if el >= 0:
#         sqrt = el ** 0.5
#         if sqrt % 1 == 0:
#             new_lst.append(el)
# print(new_lst)

#9
# arr1 = [1, 2, 3, 4, 5, 6]
# arr2 = ["a", "b", "с", "d", "e", "f"]
# arr3 = []
# for i in range(len(arr1)):
#     arr3.append(arr1[i])
#     arr3.append(arr2[i])
# print(arr3)

#10
# lst = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
# new_lst = []
# for i, el in enumerate(lst):
#     new_lst.append(len(el))
# print(f"Minimum lenght of words is {min(new_lst)}")
# print(f"Maximum lenght of words is {max(new_lst)}")

#11
# lst = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
# max_len = max(len(el) for el in lst)
# new_lst = []
# for el in lst:
#     if len(el) == max_len:
#         new_lst.append(el)
# print(new_lst)

#12
# lst = ['Apricot', 'Cat', 'Dog', 'Ocelot', 'Zebra', 'Bat', 'Orange']
# new_lst = []
# s = 0
# for i, el in enumerate(lst):
#     new_lst.append(len(el))
#     s = s + new_lst[i]
# print(f"Middle of the lenght of words is {round(s/len(lst),0)}")

#List comprehension
#1
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# new_lst = [i for i in lst if i > 0]
# print(new_lst)

#2
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# new_lst = [i for i in lst if i % 2 == 1]
# print(new_lst)

#3
# names = ["Alice", "July", "Kate", "Melissa", "Frey", "Una", "Irine"]
# voiels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# names_v = [name for name in names if name[0] in voiels]
# print(names_v)

#4
# s = 'Summer is the best season of the year'
# voiels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# letters = [l for l in s if l in voiels]
# print(letters, len(letters))

#5
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# s = 0
# for el in lst:
#     if el > 0:
#         s = s + el
# print(s)

#6
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# c = 0
# for el in lst:
#     if el % 2 == 0:
#         c += 1
# print(c)

#7
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# s = 0
# for el in lst:
#     if el < 0:
#         s = s + el
# print(s)

#8
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# sqr = [el ** 2 for el in lst]
# print(sqr)

#9
# num = 56
# num_str = str(num)
# s_num = list(num_str)
# s = 0
# for el in s_num:
#     el = int(el)
#     s = s + el
# print(s)

#10
# lst = ['Apricot', 'cat', 'Dog', 'ocelot', 'zebra', 'Bat', 'Orange']
# new_lst = []
# for word in lst:
#     if word[0].istitle():
#         new_lst.append(word)
# print(new_lst)

#11
# lst = ['Apricot', 'cat', 'Dog', 'ocelot', 'zebra', 'Bat', 'Orange']
# new_lst = [len(word) for word in lst]
# print(new_lst)

#12
# lst = ['Apricot', 'cat', 'Dog', 'ocelot', 'zebra', 'Bat', 'Orange']
# new_lst = [word for word in lst if len(word) % 2 == 0]
# print(new_lst)

#13
# lst = [0, "Hello", 1, "7", 3, True, "9th", 98, "Ms. Anderson", False, 278]
# new_lst = [el for el in lst if type(el) is int]
# print(new_lst)

#14
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# new_lst = [el * 2 if el % 2 == 0 else el * 3 for el in lst ]
# print(new_lst)

#15
# s = 'Summer is the best season of the year'
# sl = s.split()
# new_sl = []
# for word in sl:
#     if len(word) >= 5:
#         new_sl.append(word[::-1])
#     else:
#         new_sl.append(word)
# new_s = ' '.join(new_sl)
# print(new_s)

#16
# lst = [-23, 87, -100, 1, 5, 99, 45, 78, -149, 388, 599, 1024]
# new_lst = []
# for el in lst:
#     if el > 0:
#         if el % 2 == 0:
#             el = el * 2
#         else:
#             el = el * 3
#         new_lst.append(el)
# print(new_lst)