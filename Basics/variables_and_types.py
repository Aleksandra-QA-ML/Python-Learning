# Topic: Variables and Data Types
# Part of my Python learning journey for QA & ML
# from turtledemo.clock import current_day
#
print('Aleksandra')
print('Jacksonville, Fl')
print("I'm learning the programming Language Python")
print(2025)
print(2+2)
print('Today is June, 20, 2025')

import itertools as it
def two_sum(numbers, target):
    list_indices = list(range(len(numbers)))
    all_index_comb = it.combinations(list_indices, 2)
    for indices in all_index_comb:
        print(f'Indices: {indices}')
        values = tuple(numbers[i] for i in indices)
        print(values)
        current_sum = sum(values)
        if current_sum == target:
            return indices

a, b = [1, 2, 3], 4
print(two_sum(a,b))

car_made = "Toyota"
car_model = "Camry"
car_year = 2020
name = "Aleksandra"
movie = 'Mrs & Ms Smith'
magic_number = 666
price = 3.14

a = 12
b = 35
sum = a + b
subtr = a - b
mult = a * b
div = a / b
print(sum, subtr, mult, div)

num_1 = 20
num_2 = 3
div = num_1 // num_2
print(div)

num = 3
power = num ** 5
print(power)

number = 34
print(number//10, number % 10)

x = 20
x += 1
x -= 1
x *= 2
x /= 3

n = 5
k = 32
print(k//n, k%5)

