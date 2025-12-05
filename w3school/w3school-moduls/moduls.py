import mymodule
import mymodule as mx
import platform

# модуль з назвою mymodule та функція greeting
mymodule.greeting('Vasyl.')
a = mymodule.person_1['age']
print(a)
a = mymodule.person_1['country']
print(a)
a = mymodule.person_1['name']
print(a)

print('-----')

# вбудована функція для перерахування всіх імен функцій 
# (або імен змінних) у модулі. Функція dir()
# Функцію dir()можна використовувати на всіх модулях, 
# також на тих, які ви створюєте самостійно.
x = platform.system()
print(x)
x = dir(platform)
print(x)

print('-----')

# Ви можете імпортувати лише частини з модуля, використовуючи fromключове слово.
from mymodule import person_1
print(person_1['age'])
print(person_1['name'])
print(person_1['country'])

print('-----')

# exercise 1
# Напишіть програму на Python, яка використовує вбудований модуль math, щоб 
# обчислити квадратний корінь числа 225 та знайти значення pi (пі)
# 1. Імпортуємо модуль
import math

# 2. Обчислюємо квадратний корінь числа 225
number = 225
square_root = math.sqrt(number)

# 3. Отримуємо значення константи pi (пі)
pi_value = math.pi

# 4. Виводимо результат
print(f'Квадратний корінь числа {number} дорівнює {square_root}.')
print(f'Значення Пі у модулі math: {pi_value}.')

print('-----')

# exercise 2
# Створення простого користувацького модуля та імпорт його функцій.
# 1. Імпортуємо створений модуль
import my_operations

# 2. Використовуємо функції з модуля
num1 = 10
num2 = 5
sum_result = my_operations.add(num1, num2)

num3 = 4
num4 = 7
product_result = my_operations.multiplay(num3, num4)

# 3. Виводимо результати
print(f'Sum {num1} and {num2}: {sum_result}.')
print(f'Multiplay {num3} and {num4}: {product_result}.')

print('-----')


