#1
# name = 'Aleksandra Savostianova'
# fist_name = name[0:10]
# second_name = name[11:]
# email = fist_name + '.' + second_name + '@company.com'
# print(email)

#2
# time = '12:15:20'
# hours = int(time[0:2])
# minuts = int(time[3:5])
# seconds = int(time[6:])
# print(hours)
# print(minuts)
# print(seconds)
# total_seconds = hours * 360 + minuts * 60 + seconds
# print(total_seconds)

# word = input('Enter any string: ')
# if word.isdigit():
#     print(" has only digits")
# elif word.isalpha() and word.islower():
#     print(" has lowercase letters")
# elif word.isalpha() and word.isupper():
#     print(" has uppercase letters")
# elif word.isalpha() and not word.islower() and not word.isupper():
#     print(" has lowercase and uppercase letters")
# elif not word.isdigit() and not word.isalpha() and word.islower():
#     print("has digits and lowercase letters")
# elif not word.isdigit() and not word.isalpha() and word.isupper():
#     print(" has digits and uppercase letters")
# else:
#     print(" has upper and lowercase letters and digits ")

# word = 'programmer'
# n1 = word.find('r')
# n2 = word.rfind('r')
# n3 = word.index('r')
# n4 = word.rindex('r')
# print(n1)
# print(n2)
# print(n3)
# print(n4)

# s = input("Enter any word: ")
# n = 2
# print(s[n] * n)

# full_name = 'Paul Bore'
# first_name = full_name[0:4]
# second_name = full_name[5:]
# print(f'''{first_name}
# {second_name}''')

# string = input('Enter any two-word string: ')
# n = string.index(' ')
# first_word = string[0:n]
# second_word = string[n+1:]
# print(f'{second_word} {first_word}')

# text = input('Enter any three-word text: ')
# n = text.index(' ')
# s = text.rindex(' ')
# first_word = text[0:n]
# second_word = text[n+1:s]
# third_word = text[s+1:]
# print(f'{third_word} {second_word} {first_word}')

# text = input('Enter any three-word text: ')
# n = text.index(' ')
# s = text.rindex(' ')
# second_word = text[n + 1:s]
# print(second_word[::-1])

# phrase = "My eyes are green too!"
# quastion = input('What\' your favorite color? ')
# n = phrase.index('green')
# s = phrase.rindex(' ')
# first_part = phrase[0:n]
# last_part = phrase[s:]
# print(f"{first_part} {quastion} {last_part}")

# country = 'United States of America'
# print(country.count('a'))

# text = 'Have a nice day!'
# c = 'y'
# print(text.count(c))

# string = 'Once upon a time...'
# char = ' '
# length = len(string)
# count = string.count(char)/length*100
# print(round(count, 2))

# text = "If you want to be somebody, somebody really special, be yourself."
# e = text.count('e')
# o = text.count('o')
# if e > o:
#     print("e" * e)
# else:
#     print("o" * o)

# first_name = input('Enter your first_name: ')
# middle_name = input('Enter your middle_name: ')
# last_name = input('Enter your last_name: ')
# lenght = max(len(first_name), len(middle_name), len(last_name))
# print(first_name.rjust(lenght))
# print(middle_name.rjust(lenght))
# print(last_name.rjust(lenght))

# word = input("Enter any word: ")
# widht = 10
# if len(word) > widht:
#     print("Error")
# else:
#     print("*" * (widht + 2))
#     print(f'*{word.center(widht)}*')
#     print("*" * (widht + 2))

# animal = input("Enter any animal: ")
# tail = "ey"
# print(animal.endswith(tail))

# greet = input("Enter any welcome phrase: ")
# print(greet.startswith("Hello"))

# user_name = input("Enter any user name: ")
# vowels = ['a', 'e', 'i', 'o', 'u']
# if user_name[0] in vowels:
#     print(f'"{user_name}, your name starts with vowel"')
# else:
#     print(f'"{user_name}, your name starts with consonant"')

# string = input("Enter any string: ")
# numbers = str([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# if string[-1] in numbers:
#     print("Yes")
# else:
#     print("No")

# string = input("Enter any string: ")
# print("y" in string)

# string = 'Great place'
# word = 'day'
# print(word in string)

# s = '   You need to be better  '
# r = s.strip()
# t = r.title()
# Y = s.find("Y")
# R = s.find("r")
# l_count = s.count(' ', R)
# print(t + ("!" * l_count))

# text = "Summer is my favorite time of year"
# new_text = text.replace("Summer","Winter")
# print(new_text)

# s = "dog is an animal"
# new_s = s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
# print(new_s)

# string = input("Enter any string: ")
# word = input("Enter any word contained in the string: ")
# word1 = input("Enter any replace word  in the string: ")
# print(string.replace(word, word1))