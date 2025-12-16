# JSON — це синтаксис для зберігання та обміну даними.
# JSON — це текст, написаний за допомогою об'єктної нотації JavaScript.
# Python має вбудований пакет під назвою json, 
# який можна використовувати для роботи з даними JSON.

import json

# Якщо у вас є рядок JSON, ви можете його проаналізувати 
# за допомогою json.loads()методу, pезультатом буде
# Python dictionary:
# some JSON:
x = '{"name": "John", "age": 30, "city": "New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y['age'])

print('-----')

# If you have a Python object, you can convert it into 
# a JSON string by using the json.dumps() method
# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

print('-----')

# Ви можете конвертувати об'єкти Python таких типів у рядки JSON:
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

# Конвертуйте об'єкти Python у рядки JSON та виводьте значення:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas", "mango"]))
print(json.dumps(("apple", "apricot")))
print(json.dumps("Hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print('-----')

# Під час конвертації з Python у JSON, об'єкти Python 
# конвертуються в еквівалент JSON (JavaScript)
# dict - Object
# list - Array
# tuple - Array
# str - String
# int - Number
# float - Number
# True - true
# False - false
# None - null
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorsed": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))

print('-----')

# Метод json.dumps()має параметри, 
# щоб полегшити читання результату
print(json.dumps(x, indent = 4))

print('-----')

# параметр indent використовується для визначення 
# кількості відступів.
# Ви також можете визначити роздільники, значення за 
# замовчуванням (", ", ":"), що означає використання 
# коми та пробілу для розділення кожного об'єкта, 
# а також двокрапки та пробілу для розділення ключів 
# від значень: використовуємо параметр separators,
# щоб змінити роздільник за замовчуванням:
print(json.dumps(x, indent = 4, separators = (". ", " = ")))

print('-----')

# Метод json.dumps()має параметри для впорядкування ключів у результаті
# Використовуйте sort_keysпараметр, щоб вказати, чи слід сортувати результат, чи ні:
print(json.dumps(x, indent = 4, sort_keys = True))

print('-----')

# exercise 1
# Парсинг JSON-рядка та вилучення даних
# Вхідні дані (JSON-рядок):
{
    "title": "Світло в серпні",
    "year": 1932,
    "author": {
        "name": "Вільям Фолкнер",
        "nationality": "Американська"
    },
    "genres": ["Модернізм", "Південна готика"]
}

import json

def parse_book_info(json_string):
    """
    Парсить JSON-рядок та повертає інформацію про книгу.
    """
    try:
        data = json.loads(json_string)
        
        title = data['title']
        year = data['year']
        # Доступ до вкладеного словника для отримання імені автора
        author_name = data['author']['name']
        
        result = f"Назва: {title}, Рік: {year}, Автор: {author_name}"
        return result
    except json.JSONDecodeError:
        return "Помилка: Невірний JSON-формат."
    except KeyError as e:
        return f"Помилка: Відсутній ключ {e} у даних."

# Вхідні дані
json_data = '''
{
    "title": "Світло в серпні",
    "year": 1932,
    "author": {
        "name": "Вільям Фолкнер",
        "nationality": "Американська"
    },
    "genres": ["Модернізм", "Південна готика"]
}
'''

# Виконання
output = parse_book_info(json_data)
print(f"Результат: {output}")

# Перевірка:
# Назва: Світло в серпні, Рік: 1932, Автор: Вільям Фолкнер

print('-----')

# exercise 2
# Запис даних Python у JSON-файл
# Вхідні дані (Список Python):
employees = [
    {"id": 101, "name": "Олена Ковальчук", "department": "Маркетинг"},
    {"id": 102, "name": "Ігор Мельник", "department": "Розробка"},
    {"id": 103, "name": "Наталія Савченко", "department": "HR"}
]

import json
import os

def write_employees_to_json(employees_list, filename):
    """
    Записує список словників у JSON-файл з відступами.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Використовуємо json.dump для запису у файл
            # indent=4 додає гарне форматування з відступами
            json.dump(employees_list, f, ensure_ascii=False, indent=4)
        print(f"Дані успішно записано у файл '{filename}'.")
        
        # (Опціонально) Перевірка вмісту файлу для демонстрації
        # with open(filename, 'r', encoding='utf-8') as f_read:
        #     content = f_read.read()
        #     print("\nВміст файлу:")
        #     print(content)
            
    except IOError as e:
        print(f"Помилка запису файлу: {e}")

# Вхідні дані
employees = [
    {"id": 101, "name": "Олена Ковальчук", "department": "Маркетинг"},
    {"id": 102, "name": "Ігор Мельник", "department": "Розробка"},
    {"id": 103, "name": "Наталія Савченко", "department": "HR"}
]

filename = 'employees.json'

# Виконання
write_employees_to_json(employees, filename)

# Приклад вмісту файлу 'employees.json' (після виконання):
# [
#     {
#         "id": 101,
#         "name": "Олена Ковальчук",
#         "department": "Маркетинг"
#     },
#     ...
# ]

print('-----')

# exercise 3
# Читання JSON-файлу та обчислення середнього значення
# Вміст файлу scores.json:
[
    {"name": "Андрій", "score": 85},
    {"name": "Вікторія", "score": 92},
    {"name": "Сергій", "score": 78},
    {"name": "Марія", "score": 95}
]

import json
import os

# Створення файлу 'scores.json' для демонстрації (це не частина рішення, а підготовка)
file_content = """
[
    {"name": "Андрій", "score": 85},
    {"name": "Вікторія", "score": 92},
    {"name": "Сергій", "score": 78},
    {"name": "Марія", "score": 95}
]
"""
with open('scores.json', 'w', encoding='utf-8') as f:
    f.write(file_content)

def calculate_average_score(filename):
    """
    Зчитує JSON-файл з результатами та обчислює середній бал.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Використовуємо json.load для читання з файлу
            data = json.load(f)
            
        if not data:
            return "Файл порожній або не містить даних."
        
        total_score = 0
        
        # Обчислення суми балів
        for student in data:
            total_score += student['score']
            
        # Обчислення середнього
        average_score = total_score / len(data)
        
        return f"Середній бал {len(data)} студентів: {average_score:.2f}"
        
    except FileNotFoundError:
        return f"Помилка: Файл '{filename}' не знайдено."
    except json.JSONDecodeError:
        return "Помилка: Невірний JSON-формат у файлі."
    except KeyError as e:
        return f"Помилка: Відсутній ключ {e} у даних файлу."

# Виконання
filename = 'scores.json'
output = calculate_average_score(filename)
print(f"Результат: {output}")

# Перевірка:
# (85 + 92 + 78 + 95) / 4 = 350 / 4 = 87.5
# Середній бал 4 студентів: 87.50