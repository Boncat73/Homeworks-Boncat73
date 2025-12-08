# exercise 1
# Perform basic dictionary operations
# Виконання основних операцій зі словником
my_dict = {
    'name': 'Alice', 
    'age': 35, 
    'city': 'New York'}
print(f'Original dictionary: {my_dict}.')

# add a new key-value pair:
# додати нову пару ключ-значення:
my_dict['prifession'] = 'Doctor'
print(f"Update dictionary after adding 'profession': {my_dict}")

# modify value:
# змінити значення:
my_dict['age'] = 40
print(f'Update dictionary after modification:  {my_dict}.')

# print key:
# друкування ключа
print(f"'City:', my_dict['city']")

print('-----')

# exercise 2
# Perform dictionary operations
# виконання операцій зі словником:
my_dict = {
    'name': 'Alice', 
    'age': 35, 
    'city': 'New York', 
    'profession': 'Doctor'}
print(f'Original dictionary: {my_dict}.')

# remove the 'model key-value pair using del:
# видалення елемента:
del my_dict['profession']
print(f"Updated dictionary afer removing 'profession': {my_dict}.")

# printing all key-value pairs
# ітерація (прохід) по елементах
print('Printing all key-value pairs: ')
for key, value in my_dict.items():
    print(f'{key}: {value}.')

# перевірка існування ключа:
def check_key_exists(dictionary, key_to_check):
    return key_to_check in dictionary

# if 'age' in my_dict:
#     print('age exist.')

key1 = 'age'
print(f"Does '{key1}' exist? {check_key_exists(my_dict, key1)}")

print('-----')

# exercise 3
# Напишіть програму на Python для перетворення двох 
# списків Python у словник, де елементи з першого 
# списку стають ключами, а елементи з другого списку – значеннями.
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# use the zip(keys, values) to aggregate two lists
# використати zip(ключі, значення) для об'єднання двох списків
# Wrap the result of a zip() function into a dict() constructor
# Помістити результат функції zip() у конструктор dict()
# solution 1:

res_dict = dict(zip(keys, values))
print(res_dict)

#solution 2:
# empty dictionary
res_dict = dict()

for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

print('-----')

# exercise 4
# Очистити всі пари ключ-значення з заданого словника та вивести їх.
my_dict = {
    'name': 'Alice',
    'age': 35,
    'city': 'New York',
}

print(f'Dictionary: {my_dict}.')

my_dict.clear()
print(f'dictionary after removing all items: {my_dict}.')

print('-----')

# exercise 5
# Напишіть код для об'єднання двох 
# словників в новий словник та виведіть його.
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

total_dict = {**dict1, **dict2}
print(total_dict)

print('-----')

# exercise 6
# Враховуючи рядок, створіть словник, де ключі – 
# це символи, а значення – їх частоти в рядку.

# варіант 1
# функція створює словник, де ключами є символи, а значеннями - їхні 
# частоти у заданному рядку:
# Args: text(str): Вхідний рядок
# Returns: dict: Словник частот символів
def count_char_frequencies(text):
    # ініціюємо порожній словник для зберігання частот
    frequency_dict = {}
    # перебираємо кожен символ у вхідному рядку
    for char in text:
        # якщо символ вже є ключем у словнику,
        # збільшуемо його значення (частоту) на 1
        if char in frequency_dict:
            frequency_dict[char] += 1
        # Якщо символу ще немає у словнику, додаємо 
        # його як новий ключ зі значенням (частотою) 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

# Приклад використання:
input_string = 'hello world'
frequencies = count_char_frequencies(input_string)
print(f"Вхідний рядок: '{input_string}.")
print(f'Словник частот: {frequencies}.')

print('-----')

# варіант 2
# Оптимізований варіант з модуля collections класс Counter,
# який спеціально розроблений для швидкого обчислення 
# частот (хешуваних) об'єктів (включаючи символи у рядку)
from collections import Counter
input_string = 'hello world'
frequencies_counter = Counter(input_string)
print(f'\nВикористання collections.Counter: {frequencies_counter}.')
# Counter є підкласом dict, тому він працює як звичайний словник.

print('-----')

# exercise 7
# Враховуючи вкладений словник {'person': {'name': 'Alice', 'age': 30}}, 
# виведіть вік Аліси.
nested_dict = {'person': {'name': 'Alice', 'age': 30}}
# потрібно послідовно звертатися до ключів: спочатку до ключа 
# зовнішнього словника, а потім до ключа внутрішнього словника.
print(f'Nested dictioanry: {nested_dict}.')
# Спочатку звертаємося до ключа 'person',
# який повертає внутрішній словник {'name': 'Alice', 'age': 30}.
# Потім звертаємося до ключа 'age' цього внутрішнього словника.
age = nested_dict['person']['age']
print(age)

print('-----')

