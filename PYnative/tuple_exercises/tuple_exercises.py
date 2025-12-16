# exercise 1
# Виконання основних операцій з кортежами
# create a Tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"My tuple: {my_tuple}")

# access Elements
third_element = my_tuple[2] # Index 2 corresponds to the third element
print(f"The third element of my_tuple: {third_element}")

# tuple Length
tuple_length = len(my_tuple)
print(f"The length of my_tuple: {tuple_length}")

print('-----')

# exercise 2
# Повторіть наведений нижче кортеж тричі.
original_tuple = ('a', 'b')
three_tuple = original_tuple * 3
print(f'Repeated tuple: {three_tuple}')

print('-----')

# exercise 3
# Зробіть зріз кортежу, щоб отримати елементи з 4-ї по 7-му позицію.
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Slice from the 4th position (index 3) up to 
# (but not including) the 8th position (index 7)
sliced_numbers = numbers_tuple[3:7]
print(f"Sliced tuple: {sliced_numbers}")

print('-----')

# exercise 4
# Зворотний кортеж
tuple_num = (10, 20, 30, 40, 50)
tuple_num = tuple_num[::-1]
print(tuple_num)

print('-----')

# exercise 5
# Доступ до вкладених кортежів
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# understand indexing
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20
print(tuple1[1][1])

print('-----')

# exercise 6
# Створення кортежу з одним елементом 50
tuple_oun_number = (50, )
print(tuple_oun_number)

print('-----')

# exercise 7
# Розпакуйте кортеж на 4 змінні
tuple1 = (10, 20, 30, 40)

# unpack tuple into 4 variables
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

print('-----')

# exercise 8 
# Обмін двома кортежами
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)

print('-----')

# exercuse 9
# Копіювання певних елементів з кортежу
tuple1 = (11, 22, 33, 44, 55, 66)
print(f'Original tuple: {tuple1}')
tuple2 = tuple1[3:-1]
print(f'Result: {tuple2}')

print('-----')

# exercise 10
# Перетворити список my_list = [10, 20, 30]на кортеж
my_list = [10, 20, 30]
# Use the tuple() constructor to convert the list
converted_tuple = tuple(my_list)
print(f"Converted list to tuple: {converted_tuple}")

print('-----')

# exercise 11
# Напишіть функцію get_min_max(numbers), яка приймає 
# список чисел і повертає кортеж, що містить 
# мінімальне та максимальне число
def get_min_max_num(numbers):
    if not numbers:
        return (None, None) # Handle empty list case
    
    min_val = min(numbers)
    max_val = max(numbers)
    return (min_val, max_val)

# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max_num(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")

print('-----')

# exercise 12
# Порівняйте два кортежі та з'ясуйте, який з них «більший» і чому
tuple_1 = (1, 2, 3)
tuple_2 = (1, 2, 4)

print(f"Tuple 1: {tuple_1}")
print(f"Tuple 2: {tuple_2}")

if tuple_1 > tuple_2:
    print(f"{tuple_1} is greater than {tuple_2}")
elif tuple_1 < tuple_2:
    print(f"{tuple_1} is less than {tuple_2}")
else:
    print(f"{tuple_1} is equal to {tuple_2}")

print('-----')

# exercise 13
# Видалення дублікатів з кортежу
# Рішення 1: Якщо НЕ треба зберігати початковий порядок першої появи:
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")

# Convert to a set to remove duplicates (order is not preserved)
unique_elements_set = set(my_tuple)

# Convert back to a tuple
unique_tuple = tuple(unique_elements_set)
print(f"Tuple with unique elements: {unique_tuple}")

# Рішення 2 : Якщо важливо зберегти початковий порядок першої появи:
from collections import OrderedDict
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")

unique_ordered_tuple = tuple(OrderedDict.fromkeys(my_tuple))
print(f"Tuple with unique elements (order preserved): {unique_ordered_tuple}")

print('-----')

# exercise 14
# Напишіть код для фільтрації студентів з балами менше 90 зі заданого списку кортежів
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")

high_achievers_loop = []
for student in students:
  if student[1] >= 90:
    high_achievers_loop.append(student)
print(f"Students with scores 90 or above (loop method): {high_achievers_loop}")

print('-----')

# exercise 15
# Дано кортеж чисел, створіть новий кортеж, де кожне число зведено до квадрата
# Рішення 1 : Використання map() та tuple()
t = (1, 2, 3, 4)
print(f"Original tuple: {t}")

# Method 1: Using map() and tuple()
squared_tuple_map = tuple(map(lambda x: x**2, t))
print(f"Squared tuple (map function): {squared_tuple_map}")

# Рішення 2 : Використання циклу
# 7. Map Tuples
t = (1, 2, 3, 4)
print(f"Original tuple: {t}")

# Method 2: Using a loop
squared_list_loop = []
for num in t:
  squared_list_loop.append(num ** 2)
  squared_tuple_loop = tuple(squared_list_loop)
print(f"Squared tuple (loop): {squared_tuple_loop}")

print('-----')

# exercise 16
# Дано вкладений кортеж. Напишіть програму для зміни 
# першого елемента (22) списку всередині наступного 
# кортежу на 222
tuple1 = (11, [22, 33], 44, 55)
print(f'Original tuple: {tuple1}')
tuple1[1][0] = 222
print(tuple1)

print('-----')

# exercise 17
# Сортування кортежу кортежів за другим елементом
# 1. Sort a tuple by 2nd item
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print(f"Original tuple: {tuple1}")

# Convert the tuple to a list because tuples are 
# immutable and cannot be sorted in-place
list1 = list(tuple1)

# Sort the list using the 'sorted()' function with 
# a lambda key
# The lambda function `lambda item: item[1]` tells 
# sorted() to use the second element
# (index 1) of each inner tuple for comparison.
sorted_list = sorted(list1, key=lambda item: item[1])

# If you need the result back as a tuple, convert 
# the sorted list back to a tuple
sorted_tuple = tuple(sorted_list)

print(f"Sorted tuple by 2nd item: {sorted_tuple}")

print('-----')

# exercise 18
# Напишіть код для підрахунку кількості входжень 
# елемента 50 з кортежу
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

print('-----')

# exercise 19
# Перевірте, чи всі елементи в кортежі однакові
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))