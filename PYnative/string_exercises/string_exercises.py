print("This is a string. It is a type data in Python.")
print('This is also a string. It is also a type data in Python.')
print('-' * 30)
name = "Strong string."
print(name.title())
print(name.capitalize())
print(name.casefold())
#print(name.center()) ???
print(name.count)
print(name.encode())
#print(name.endswith()) ???
print(name.expandtabs())
#print(name.find()) ???
print(name.format())
#print(name.format_map()) ???
#print(name.index()) ???
print(name.isalnum())
print(name.lower())
print(name.upper())

print('-' * 30)

#variables in string
first_name = "Vasyl"
second_name = "Bondarevskyi"
full_name = f"{first_name} {second_name}"
print(first_name)
print(second_name)
print(full_name)
#age_user_1 = input(print("Where are you old?"))
#print(f"You are {full_name}, you have {age_user_1} years old.")
print(f"Your name is title: {full_name.title()}")
print(f"Your name is upper: {full_name.upper()}")
print(f"Your name is lower: {full_name}")
print(f"Your name is capitalize: {full_name}")

print('-' * 30)

print('Languages:\nPython\nC\nJavaScript')
print('Python\nC\nJava\nJavaScript')
print('\n\tPython\n\tC\n\tJava\n\tJavaScript')

# exercise 1a
# Створіть рядок, що складається з першого, 
# середнього та останнього символів
str_1 = 'James'
print("Original String is", str_1)

# отримуємо перший символ
res = str_1[0]

# отримуємо довжину рядка
l = len(str_1)
# отримуємо індекс середнього символу
mi = int(l / 2)
# отримуємо середній символ та додаємо його до результату
res = res + str_1[mi]

# отримуємо останній символ та додаємо його до результату
res = res + str_1[l - 1]

print("New String:", res)

print('-----')

# exercise 1b
# Напишіть програму для створення нового рядка з трьох 
# середніх символів вхідного рядка
string_1 = 'JhonDipPeta'
string_2 = 'JaSonAy'
def get_middle_three_chars(string_1):
    print("Original String is", string_1)

    # отримуємо індекс середнього символу
    mi = int(len(string_1) / 2)

    # використовуємо розріз рядка для отримання
    # символів результату
    res = string_1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")

print('-----')

# exercise 2
# Додати новий рядок посередині заданого рядка
str1 = 'Ault'
str2 = 'Kelly'
def append_middle(s1, s2):
    print("Original Strings are", s1, s2)

    # індекс середнього символу s1
    mi = int(len(s1) / 2)

    # отримуємо символ від 0 до середнього індексу
    x = s1[:mi:]
    # поєднуємо s2 з цим символом
    x = x + s2
    # додаємо символ,що залишився з s1
    x = x + s1[mi:]
    print("After appending new string in middle:", x)

append_middle("Ault", "Kelly")

print('-----')

# exercise 3
# Для двох рядків, s1 та s2, напишіть програму, яка 
# повертатиме новий рядок, що складається з першого, 
# середнього та останнього символів s1 та s2.
s1 = 'America'
s2 = 'Japan'
def mix_str(s1, s2):
    # get first character from both string
    first_char = s1[0] + s2[0]

    # get middle character from both string
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]

    # get last character from both string
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]

    # add all
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_str(s1, s2)

print('-----')

# exercise 4
# Розташуйте символи рядка таким чином, щоб 
# малі літери були першими
str1 = 'PyNaTive'
print('Original String: ', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to upper list
        upper.append(char)

# join both list
sorted_str = ''.join(lower + upper)
print('Result: ', sorted_str)

print('-----')

# exercise 5
# Порахуйте всі літери, цифри та спеціальні 
# символи у заданому рядку
str2 = 'P@#yn26at±&i5ve'
def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is special symbol
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)

sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)

print('-----')

# exercise 6
# Дано два рядки, s1 та s2. Напишіть програму для 
# створення нового рядка s3, який складається з 
# першого символу s1, потім останнього символу s2, 
# потім другого символу s1 та передостаннього 
# символу s2 і так далі. Будь-які залишки символів 
# йдуть в кінець результату.
sym1 = 'Abc'
sym2 = 'Xyz'
# get string length
sym1_length = len(sym1)
sym2_length = len(sym2)

# get length of a bigger string
length = sym1_length if sym1_length > sym2_length else sym2_length
result = ""

# reverse s2
sym2 = sym2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < sym1_length:
        result = result + sym1[i]
    if i < sym2_length:
        result = result + sym2[i]

print(result)

print('-----')

# exercise 7
# Напишіть програму, яка перевіряє, чи збалансовані 
# два рядки. Наприклад, рядки s1 та s2 збалансовані, 
# якщо всі символи з s1 присутні в s2. Позиція символу 
# не має значення.
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

print('-----')

# exercise 8
# Напишіть програму, яка знаходить усі входження 
# слова «USA» у заданому рядку, ігноруючи регістр літер
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

# convert string to lowercase
temp_str = str1.lower()

# use count function
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

print('-----')

# exercise 9
# Для заданого рядка s1 напишіть програму, яка 
# повертає суму та середнє значення цифр у рядку, ігноруючи всі інші символи.
input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)

print('-----')

# exercise 10
# Напишіть програму для підрахунку входжень 
# усіх символів у рядку
str1 = "Apple"

# create a result dictionary
char_dict = dict()

for char in str1:
    count = str1.count(char)
    # add / update the count of a character
    char_dict[char] = count
print('Result:', char_dict)

print('-----')

# exercise 11
# Змінити заданий рядок у зворотному порядку
str1 = 'PYnative'
# Рішення 1: Розрізання негативного рядка
print('Original string is: ', str1)

str1 = str1[::-1]
print('Reverse string is: ', str1)

# Рішення 2: Використання reversed()функції
print('Original string is: ', str1)

str1 = ''.join(reversed(str1))
print('Reverse string is: ', str1)

print('-----')

# exercise 12
# Знайдіть останню позицію заданого підрядка
str2 = 'Emma is a data scientist who knows Python. Emma works at google.'
print('Original string is: ', str2)
index = str2.rfind('Emma')
print('Last occurrence of Emma starts at index: ', index)

print('-----')

# exercise 13
# розбиття заданого рядка на дефіси та відображення кожного підрядка.
str3 = 'Emma-is-a-data-scientist'
print('Original string is: ', str3)

# split string
sub_string = str3.split('-')

print('Displaying each substring')
for sub in sub_string:
    print(sub)

print('-----')

# exercise 14
# Видалення порожніх рядків зі списку рядків
str_list = ['Emma', 'Jon', 'Kelly', None, 'Eric', '']

# Рішення 1 : Використання циклу та if умови
res_list = []
for s in str_list:
    # check for non empty string
    if s:
        res_list.append(s)
print(res_list)

# Рішення 2 : Використання вбудованої функціїfilter()
# use built-in function filter to filter empty value
new_str_list = list(filter(None, str_list))
print('After removing empty strings')
print(new_str_list)

print('-----')

# exercise 15
# Видалення спеціальних символів / розділових знаків з рядка
str4 = '/*Jon is @developer & musician'
# Рішення 1 : Використовуйте рядкові функції translate()та maketrans()
# Константа string.punctuationмістить усі спеціальні символи.
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)

# Рішення 2: Використання шаблону заміни регулярних виразів у рядку
import re

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is ", res)

print('-----')

# exercise 16
# Видалення всіх символів з рядка, крім цілих чисел
str5 = 'I am 25 years and 10 months old.'
print("Original string is", str5)

# Retain Numbers in String
# Using list comprehension + join() + isdigit()
res = "".join([item for item in str5 if item.isdigit()])

print(res)

print('-----')

# exercise 17
# Знайдіть слова, що містять як алфавіти, так і цифри
str1 = 'Emma25 is Data scientist50 and AI Expert'
res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)

print('-----')

# exercise 18
# Замініть кожен спеціальний символ на # у наступному рядку
str7 = '/*Jon is @developer & musician!!'
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)