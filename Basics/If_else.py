#1
# word = input("Enter any word: ")
# n = 2
# if 0 <= n < len(word):
#     print(f"{word[n]}")
# else:
#     print("Index is not valid")

#2
# char = input("Enter any symbol: ")
# if char.lower() in ["a","e","o","u","i"] or char.upper() in ["A","E","O","I","U"]:
#     print("Yes")
# else:
#     print("Symbol is not valid")

#3
# name = input("Enter any name: ")
# if name.lower() in ["a","e","o","u","i"] or name.upper() in ["A","E","O","I","U"]:
#     print("Yes")
# else:
#     print("No")

#4
# string = input("Enter any string: ")
# if string[-1] in ["0","1","2","3","4","5","6","7","8","9"]:
#     print("Yes")
# else:
#     print("No")

#5
# name = input("Enter any name: ")
# if len(name) > 5:
#     print("Your name is long!")
# else:
#     print("Your name is short!")

#6
# answer = input("Are you ok?: ")
# if answer == "No" or answer == "no":
#     print("Get better!")
# else:
#     print("Cool!")

#7
# a = 3
# b = 1
# if b != 0:
#     print(a/b)
# else:
#     print("Error: Cannot divide by zero.")

#8
# name = input("Enter any name: ")
# time = int(input("Enter any hour from 0 to 24: "))
# if 0<= time <= 6:
#     print(f"Good night, {name}!")
# elif 7<= time <= 11:
#     print(f"Good morning, {name}!")
# elif 12<= time <= 18:
#     print(f"Good day, {name}!")
# elif 19<= time <= 24:
#     print(f"Good night, {name}!")
# else:
#     print("Wrong time")

#9
# a = 12
# b = 24
# opperation = "*"
# result = a * b
# print(f"{a} {opperation} {b} = {result}")

#10
# price = float(input("Enter any price, $: "))
# if price >= 300:
#     print(f"You got the discount 30%, and your total price is ${price - price * 0.3}")
# elif  price >= 200:
#     print(f"You got the discount 20%, and your total price is ${price - price * 0.2}")
# elif  price >= 100:
#     print(f"You got the discount 10%, and your total price is ${price - price * 0.1}")
# else:
#     print(f"Your total price is ${price}")

#11
# age = int(input("Enter your age: "))
# if age < 16:
#     print("Children")
# elif age < 50:
#     print("Young man")
# else:
#     print("Senior")

#12
# current_color = input("Current color of traffic light is ")
# if current_color == "red":
#     print("Next color of traffic light will be green")
# elif current_color == "yellow":
#     print("Next color of traffic light will be red")
# elif current_color == "green":
#     print("Next color of traffic light will be yellow")

# _1
# t = float(input("Enter the temperature of body: "))
# if t < 37:
#     health = "healthy"
#     print(health)
# else:
#     health = "ill"
#     print(health)
# health = "healthy" if t < 37 else  "ill"
# print(health)

#_2
# num_of_day = int(input('Enter the number of the day of week: '))
# if num_of_day in [6, 7]:
#     day = 'Weekend'
#     print(day)
# else:
#     day = 'Work day'
#     print(day)

# day = 'Weekend' if num_of_day == 6 or num_of_day == 7 else 'Work day'
# print(day)

#_3
# number = int(input('Enter any number: '))
# if number >= 0:
#     number *= 2
#     print(number)
# else:
#     print(abs(number))
# print(number * 2) if number >= 0 else print(abs(number))

#_4
# n = int(input('Enter any number: '))
# if n % 9 == 0:
#     is_lucky = "Lucky number"
# else:
#     is_lucky = "Not lucky number"
# print(is_lucky)
# is_lucky = "Lucky number" if n % 9 == 0 else "Not lucky number"
# print(is_lucky)