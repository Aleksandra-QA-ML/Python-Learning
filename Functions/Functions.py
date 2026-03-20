#1
# def greet(w):
#     return w
#
# print(greet("Hello world!"))

#2
# def hello_user(name):
#     return f"Hello {name}"
#
# print(hello_user("Dasha"))

#3
# def say_hello(name, time):
#     if  time in range(6):
#         return f"Good night, {name}!"
#     elif time in range(7, 11):
#         return f"Good morning, {name}!"
#     elif time in range(12, 18):
#         return f"Good day, {name}!"
#     else:
#         return f"Good evening, {name}!"
#
# print(say_hello("Alex", 2))
# print(say_hello("Pedro", 10))
# print(say_hello("Felix", 14))
# print(say_hello("Tristan", 22))

#4
# def product(a, b, c):
#     return a * b * c
#
# print(product(2, 4, 5))

#5
# def opposite(x):
#     return x * -1
#
# print(opposite(-2))
# print(opposite(4))

#6
# def distance_from_origin(x,y):
#     return (x**2 + y**2)**0.5
#
# print(round((distance_from_origin(5,7)),1))

#7
# def distance(x1,y1,x2,y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
#
# print(round((distance(3.5,7,9.9,4)),1))

#8
# def percentage(number, percent):
#     return number * (percent/100)
#
# print(percentage(350,10))

#9
# def body_mass_index(weight, height):
#     return weight/(height**2)
#
# print(round((body_mass_index(59, 1.75)),1))

#10
# def average(a, b):
#     return (a + b)/ 2
#
# print(average(3, 7))

#11
# def geometric_mean(num1, num2):
#     return (num1 * num2)**0.5
#
# print(geometric_mean(5, 7))

#12
# def angles_of_polygon(n):
#     return 180 * (n - 2)
#
# print(angles_of_polygon(7))

#13
# def miles_to_feet(miles):
#     return miles * 5280
#
# print(miles_to_feet(5))

#14
# def centigrade(tempF):
#     return (tempF - 32) * (5/9)
#
# print(round((centigrade(90)),1))

#15
# def fahrenheit(tempC):
#     return 32 + (tempC * 9/5)
#
# print(round((fahrenheit(24)),1))

#if-else
#1
# def even_odd(number):
#     return "Even" if number % 2 == 0 else "Odd"
#
# print(even_odd(6))

#2
# def lucky_number(num):
#     return "True" if num % 9 == 0 else "False"
#
# print(lucky_number(99))

#3
# def negative(x):
#     return x * -1 if x > 0 else x
#
# print(negative(45))

#4
# def operation(a,b):
#     return a + b, a - b , a * b, a / b, a % b, a // b
#
# print(operation(4,5))

#5
# def figure(length, weight):
#     return length * weight if length == weight else (length + weight) * 2
#
# print(figure(4,6))
# print(figure(7,7))

#6
# def division(x,y):
#     return "True" if y != 0 else "Error"
#
# print(division(2,-5))
# print(division(2,0))

#7
# def division(n,a,b):
#     if a != 0 and b != 0:
#         return "True"
#
# print(division(3,6,0))
# print(division(3,6,9))

#8
# def triangle(a,b,c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return "False"
#     if a + b > c and \
#         a + c > b and \
#         b + c > a:
#         return "True"
#     else:
#         return "False"
#
# print(triangle(3,5,9))
# print(triangle(3,8,4))
# print(triangle(-3,5,9))
# print(triangle(3,5,4))

#9
# def final_grade(exam_grade, projects):
#     if projects >= 10 and exam_grade >= 90:
#         return 100
#     elif projects >= 5 and exam_grade >= 75:
#         return 90
#     elif projects >= 2 and exam_grade >= 50:
#         return 75
#     else:
#         return 0
#
# print(final_grade(95, 11))
# print(final_grade(78, 6))
# print(final_grade(66, 4))
# print(final_grade(45, 1))
# print(final_grade(95, 1))

#10
# def income(salary, bonus):
#     return salary * 5 if bonus == True else salary
#
# print(income(9000, True))
# print(income(9000, False))

#11
# def sale_cakes(n):
#     if n >= 10:
#         return f"{90 * n} cents"
#     elif 5 <= n < 10:
#         return f"{95 * n} cents"
#     else:
#         return f"{100 * n} cents"
#
# print(sale_cakes(1))
# print(sale_cakes(5))
# print(sale_cakes(15))

#12
# def planet_name(n):
#     if n == 1:
#         return "Mercury"
#     elif n == 2:
#         return "Venus"
#     elif n == 3:
#         return "Earth"
#     elif n == 4:
#         return "Mars"
#     elif n == 5:
#         return "Jupiter"
#     elif n == 6:
#         return "Saturn"
#     elif n == 7:
#         return "Uranus"
#     elif n == 8:
#         return "Neptune"
#     else:
#         return
#
# print(planet_name(1))
# print(planet_name(2))
# print(planet_name(3))
# print(planet_name(4))
# print(planet_name(5))
# print(planet_name(6))
# print(planet_name(7))
# print(planet_name(8))
# print(planet_name(9))

# def planet_name(n):
#     name = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
#     return name[n-1] if 1 <= n <= len(name) else "Неизвестный номер планеты. Введите число от 1 до 8."
#
# print(planet_name(1))
# print(planet_name(2))
# print(planet_name(3))
# print(planet_name(4))
# print(planet_name(5))
# print(planet_name(6))
# print(planet_name(7))
# print(planet_name(8))
# print(planet_name(9))

#13
# def grade(s1, s2, s3):
#     score = (s1 + s2 + s3)/3
#     if 90 <= score <= 100:
#         return "A"
#     elif 80 <= score < 90:
#         return "B"
#     elif 70 <= score < 80:
#         return "C"
#     elif 60 <= score < 70:
#         return "D"
#     else:
#         return "F"
#
# print(grade(40,78,90))
# print(grade(90,92,90))
# print(grade(85,78,90))
# print(grade(76,64,80))
# print(grade(65,73,71))

#14
# def discr_bmi(weight, height):
#     bmi = weight / (height ** 2)
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 25.0:
#         return "Normal"
#     elif bmi <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"
#
# print(discr_bmi(90, 1.45))
# print(discr_bmi(90, 1.75))
# print(discr_bmi(90, 1.95))
# print(discr_bmi(90, 2.25))

#15
# def discr_age(age):
#     if age <= 12:
#         return "You're a kid"
#     elif 13 <= age <= 17:
#         return "You're a teenager"
#     elif 18 <= age <= 64:
#         return "You're an adult"
#     else:
#         return "You're an elderly"
#
# print(discr_age(90))
# print(discr_age(55))
# print(discr_age(15))
# print(discr_age(10))

#16
# def word(n):
#     num = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     return num[n] if 0 <= n < len(num) else "None. Enter number from 0 to 9."
#
# print(word(0))
# print(word(1))
# print(word(2))
# print(word(3))
# print(word(4))
# print(word(5))
# print(word(6))
# print(word(7))
# print(word(8))
# print(word(9))
# print(word(10))

#17
# def square_of_triangle(a, b, c):
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     if a <= 0 or b <= 0 or c <= 0:
#         return "The triangle does not exist"
#     if a + b > c and a + c > b and b + c > a:
#         return area
#     else:
#         return "The triangle does not exist"
#
# print(round((square_of_triangle(2, 4, 3)),1))
# print(square_of_triangle(2, 4, 7))
# print(square_of_triangle(2, -4, 3))

#комбинированные циклы
#1
# def get_sum(a, b):
#     s = 0
#     start = min(a, b)
#     end = max(a, b)
#     for i in range(start, end + 1):
#         s += i
#     return s
#
# print(get_sum(4, 8))

#2
# def summation(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += i
#
#     return s
# print(summation(90))

#3
# def describesNumber(number):
#     if number > 0 and number % 2 == 0:
#         return "Even positive number"
#     elif number < 0 and number % 2 == 0:
#         return "Even negative number"
#     elif number > 0 and number % 2 == 1:
#         return "Odd positive number"
#     elif number < 0 and number % 2 == 1:
#         return "Odd negative number"
#     else:
#         return "Zero"
#
# print(describesNumber(12))
# print(describesNumber(-12))
# print(describesNumber(555))
# print(describesNumber(-99))
# print(describesNumber(0))

#4
# def power_of_5(x):
#     while x > 1:
#         x = x / 5
#     return x == 1
#
# print(power_of_5(25))
# print(power_of_5(115))

#5
# def count_division(n):
#     s = 0
#     for i in range(1, n + 1, 1):
#         if n % i == 0:
#             s += 1
#     return s
#
# print(count_division(10))
# print(count_division(100))

#6
# def simple_num(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, (n // 2) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# print(simple_num(2))
# print(simple_num(-3))
# print(simple_num(1))
# print(simple_num(19))
# print(simple_num(13))

#1
# def reverse(words):
#     s = ''
#     for letter in words:
#         if letter.islower():
#             s += letter.upper()
#         elif letter.isupper():
#             s += letter.lower()
#         else:
#             s += letter
#     return s
#
# print(reverse('SuMmeR Time'))

#2
# def kebab_to_snake(str):
#     s = ''
#     for char in str:
#         if char == '-':
#             s += char.replace('-', '_')
#         else:
#             s += char
#     return s
#
# print(kebab_to_snake('kebab-to-snake'))

#3
# def count(str):
#     x = 0
#     for i in str:
#         if i.isdigit():
#             x += 1
#         else:
#             x = x
#     return x
#
# print(count('Today is 24 July of 2025'))
# print(count('I am 33 years old'))

#4
# def phone(num):
#     return f"+({num[0:3]}) {num[3:6]}-{num[6:8]}-{num[8:]}"
#
# print(phone('1234567890'))

#5
# def letters(word):
#     s = ''
#     for i in word:
#         if i in ['a', 'e', 'i', 'o', 'u']:
#             s = s + i.replace(i, '')
#         else:
#             s += i
#     return s
#
# print(letters('Nobody'))