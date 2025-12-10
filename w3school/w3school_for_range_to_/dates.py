import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))
y = datetime.datetime(2020, 7, 14)
print(y)
print(y.strftime('%B'))

print('-----')



# exercise 1
# Обчислення різниці у днях
# Напишіть функцію Python, яка приймає дві дати у форматі рядка 
# YYYY-MM-DD і повертає кількість повних днів між цими датами.
from datetime import datetime

# -> - позначка,який тип даних очікується на виході з функції чи методу
def calculate_day_difference(date_str1: str, date_str2: str) -> int:
    # обчислює кількість днів між двома датами у форматі: YYYY-MM-DD
    # Args:
    # date_str1: перша дата (рядок)
    # date_str2: друга дата (рядок)
    # Returns:
    # Кількість днів між датами (ціле число)
    try:
        # 1. Перетворення рядків у об'єкти date
        date1 = datetime.strptime(date_str1, '%Y-%m-%d').date()
        date2 = datetime.strptime(date_str2, '%Y-%m-%d').date()

        # 2. Обчислення різниці (timedelta)
        time_difference = date2 - date1

        # 3. Повернення кількості днів (абсолютне значення)
        return abs(time_difference.days)
    except ValueError as e:
        return f'Помилка формату дати: {e}'
    
# Приклад використання:
date_a = '2023-11-18'
date_b = '2025-07-09'
difference = calculate_day_difference(date_a, date_b)

print(f'Дати: {date_a} та {date_b}.')
print(f'Різниця між датами: {difference} днів.')

# зворотний порядок
date_c = '2025-05-15'
date_d = '2025-05-01'
difference_2 = calculate_day_difference(date_c, date_d)

print(f'Дати: {date_c} та {date_d}.')
print(f'Різниця між датами: {difference_2} днів.')

print('-----')

# exercise 2
# Визначення дня тижня та форматування Напишіть функцію, 
# яка приймає дату у форматі DD.MM.YYYY і повертає цю дату 
# у повному текстовому форматі, що включає назву дня тижня.
from datetime import datetime
import locale

def format_date_with_weekday(date_str: str) -> str:
    """
    Форматує дату 'DD.MM.YYYY', включаючи назву дня тижня.
    Args:
        date_str: Дата у форматі 'DD.MM.YYYY'.
    Returns:
        Відформатований рядок дати.
    """
    # Встановлення локалі для коректного виведення назв днів/місяців українською
    # Примітка: 'uk_UA.UTF-8' або 'ukr_ukr' можуть працювати в залежності від ОС.
    try:
        # Спроба встановити українську локаль
        locale.setlocale(locale.LC_TIME, 'uk_UA.UTF-8')
    except locale.Error:
        try:
            # Спроба іншого варіанту
            locale.setlocale(locale.LC_TIME, 'ukr_ukr')
        except locale.Error:
            # Якщо не вдалося, використовуємо системну локаль (може бути не укр.)
            pass 
            # print("Попередження: Не вдалося встановити українську локаль.")
            
    try:
        # 1. Перетворення рядка у об'єкт datetime
        dt_object = datetime.strptime(date_str, '%d.%m.%Y')
        
        # 2. Форматування:
        # %A - повна назва дня тижня
        # %d - день
        # %B - повна назва місяця
        # %Y - рік
        formatted_date = dt_object.strftime('%A, %d %B %Y')
        
        return formatted_date.capitalize() # Робимо першу літеру великою
    except ValueError as e:
        return f"Помилка формату дати: {e}"

# Приклад використання:
input_date = "01.01.2025"
formatted_output = format_date_with_weekday(input_date)

print(f"Вхідна дата: {input_date}")
print(f"Відформатована дата: {formatted_output}")

# Приклад 2:
input_date_2 = "31.12.2024"
formatted_output_2 = format_date_with_weekday(input_date_2)

print(f"\nВхідна дата: {input_date_2}")
print(f"Відформатована дата: {formatted_output_2}")

print('-----')

# exercise 3
# Додавання робочих днів Напишіть функцію, яка приймає початкову дату 
# (datetime.date) і кількість робочих днів, які потрібно додати. 
# Функція повинна повернути нову дату, ігноруючи суботи та неділі.
from datetime import date, timedelta

def add_working_days(start_date: date, days_to_add: int) -> date:
    """
    Додає вказану кількість робочих днів до початкової дати,
    ігноруючи суботи (6) та неділі (7).
    Args:
        start_date: Початкова дата (об'єкт date).
        days_to_add: Кількість робочих днів для додавання.
    Returns:
        Нова дата (об'єкт date).
    """
    current_date = start_date
    days_added = 0
    
    # 1. Продовжуємо додавати по одному дню, поки 
    # не набереться потрібна кількість робочих днів
    while days_added < days_to_add:
        current_date += timedelta(days=1)
        
        # 2. weekday() повертає: 0=Понеділок, 1=Вівторок, ..., 
        # 5=Субота, 6=Неділя
        weekday = current_date.weekday()
        
        # 3. Якщо день не є суботою (5) або неділею (6), 
        # зараховуємо його як робочий
        if weekday < 5: 
            days_added += 1
            
    return current_date

# Приклад використання:
start_d = date(2025, 12, 18) # Середа
days_to_add = 5 

# 18.12 (Ср) + 5 робочих днів
# 19.12 (Чт) - 1
# 20.12 (Пт) - 2
# 21.12 (Сб) - пропуск
# 22.12 (Нд) - пропуск
# 23.12 (Пн) - 3
# 24.12 (Вт) - 4
# 25.12 (Ср) - 5
end_d = add_working_days(start_d, days_to_add)

print(f"Початкова дата: {start_d.isoformat()} ({start_d.strftime('%A')})")
print(f"Кількість робочих днів для додавання: {days_to_add}")
print(f"Кінцева дата: {end_d.isoformat()} ({end_d.strftime('%A')})")

# У задачах використовуються ключові основи модуля datetime:

# Задача 1: Обчислення різниці — Використовує datetime.strptime() для 
# перетворення рядка в об'єкт, а також різницю об'єктів для отримання 
# timedelta. Це фундаментальні навички.

# Задача 2: Форматування — Використовує datetime.strptime() для парсингу 
# (розбору) і strftime() для виводу дати у бажаному форматі. Це критично 
# важливо для роботи з користувацьким інтерфейсом.

# Задача 3: Робочі дні — Включає використання timedelta для ітерації, 
# а також методу weekday() для прийняття логічних рішень (ігнорування вихідних).
# Це поєднує знання про дати з базовою логікою циклів.