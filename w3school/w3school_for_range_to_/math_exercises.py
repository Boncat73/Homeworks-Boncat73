import math
# math
# min and max numbers
x = min(5, 10, 15)
y = min(48, 56, 98)
print(x)
print(y)
print(x, y)

# absolute (positive) value
t = abs(-7.25)
print(t)

# 4 * 4 * 4
p = pow(4, 3)
print(p)

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # return 2
print(y) # return 1

x = math.pi
print(x)

print('-----')

# exercise 1
# Напишіть функцію calculate_rectangle_properties(length, width),
# яка приймає довжину та ширину прямокутника 
# (числа з плаваючою комою) і повертає кортеж (tuple), 
# що містить його площу та периметр

# Потім використайте цю функцію для знаходження площі та 
# периметру прямокутника з довжиною 12.5 та шириною 6.8
def calculate_rectangle_properties(length, width):
    """
    Обчислює площу (length * width) та периметр (2 * (length + width)) 
    прямокутника і повертає їх у вигляді кортежу.
    """
    # Формули:
    area = length * width
    perimeter = 2 * (length + width)
    
    # Повертаємо результати у вигляді кортежу (area, perimeter)
    return (area, perimeter)

# Вхідні дані
l = 12.5
w = 6.8

# Виклик функції та розпакування кортежу в окремі змінні (більш "пайтонічний" підхід)
rectangle_area, rectangle_perimeter = calculate_rectangle_properties(l, w)

# Вивід результатів
print(f"--- Завдання 1 ---")
print(f"Довжина (l): {l}, Ширина (w): {w}")
print(f"Площа прямокутника: {rectangle_area}")
print(f"Периметр прямокутника: {rectangle_perimeter}")

print('-----')

# exercise 2
# Напишіть функцію is_armstrong_number(n), яка перевіряє,
# чи є задане ціле число $N$ числом Армстронга 
# (також відоме як нарцисичне число).
# Число Армстронга — це число, яке дорівнює сумі своїх 
# цифр, кожна з яких піднесена до степеня, рівного 
# кількості цифр у цьому числі.
def is_armstrong_number(n: int) -> bool:
    """
    Перевіряє, чи є число N числом Армстронга.
    """
    # 1. Перетворюємо число на рядок, щоб легко визначити його довжину (кількість цифр)
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = 0
    
    # 2. Перебираємо кожну цифру в рядку
    for digit_char in num_str:
        # Перетворюємо символ цифри назад у ціле число
        digit = int(digit_char)
        
        # 3. Підносимо цифру до степеня num_digits і додаємо до суми
        sum_of_powers += digit ** num_digits
        
    # 4. Порівнюємо початкове число з обчисленою сумою
    return n == sum_of_powers

# Тестування
num1 = 153
num2 = 371 # 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371 (теж число Армстронга)
num3 = 123

print(f"\n--- Завдання 2 ---")
print(f"Число {num1} є числом Армстронга: {is_armstrong_number(num1)}")
print(f"Число {num2} є числом Армстронга: {is_armstrong_number(num2)}")
print(f"Число {num3} є числом Армстронга: {is_armstrong_number(num3)}")

print('-----')

# exercise 3
# Напишіть функцію geometric_sum(a, r, n), яка обчислює 
# суму перших $N$ членів геометричної прогресії
def geometric_sum(a, r, n):
    """
    Обчислює суму перших N членів геометричної прогресії:
    S_n = a * (r ** n - 1)/(r - 1)
    r != 1, a — перший член, r — знаменник, n — кількість членів.
    """
    # Перевірка на випадок r = 1 (сума буде просто n * a)
    if r == 1:
        return n * a
    
    # Використання математичної формули 
    # (використовуємо оператор ** для піднесення до степеня)
    # Змінна r_power_n = r**n (знаменник r у степені n)
    sum_n = a * (r**n - 1) / (r - 1)
    
    return sum_n

# Вхідні дані
first_term = 2  # a
common_ratio = 3  # r
num_terms = 5  # n

# Виклик функції
s5 = geometric_sum(first_term, common_ratio, num_terms)

print(f"\n--- Завдання 3 ---")
print(f"a = {first_term}, r = {common_ratio}, n = {num_terms}")
print(f"Сума S_{num_terms} = {s5}")