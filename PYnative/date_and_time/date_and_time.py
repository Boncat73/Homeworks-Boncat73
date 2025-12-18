# exercise 1
# Виведення поточної дати та часу
# варіант 1:
import datetime
# print date and time
print(datetime.datetime.now())
# only time
print(datetime.datetime.now().time())

# варіант 2:
from time import gmtime, strftime
print(strftime('%Y-%m-%d %H:%M:%S', gmtime()))

print('-----')

# exercise 2
# Напишіть код для перетворення заданої дати у 
# рядковому форматі в DateTimeоб'єкт Python.

from datetime import datetime
date_string = 'Feb 25 2020 4:20PM'
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

print('-----')

# exercise 3
# Напишіть код для віднімання тижня (7 днів) 
# від заданої дати
from datetime import datetime, timedelta
given_date = datetime(2020, 2, 25)
print('Given_date', given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print(f'New date: {res_date}')

print('-----')

# exercise 4
# Форматування дати та часу
from datetime import datetime
given_date_1 = datetime(2020, 2, 25)
print(f'Given date is: {given_date.strftime('%A %d %B %Y')}')

print('-----')

# exercise 5
# Напишіть код для знаходження дня тижня для заданої дати.
# варіант 1:
from datetime import datetime
given_date_2 = datetime(2020, 7, 26)
# to get weekday as integer
print(given_date_2.today().weekday())
# to get the english name of the weekday
print(given_date_2.strftime('%A'))

# варіант 2:
import calendar
from datetime import datetime
given_date_2 = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date_2.weekday()]
print(weekday)

print('-----')

# exercise 6
# Напишіть код, щоб додати тиждень (7 днів) та 
# 12 годин до заданої дати
# 2020-03-22 10:00:00
from datetime import datetime, timedelta
given_date_3 = datetime(2020, 3, 22, 10, 00, 00)
print(f'Given date: {given_date_3}')
days_to_add = 7
res_date_1 = given_date_3 + timedelta(days=days_to_add, hours = 12)
print(f'New Date: {res_date_1}')

print('-----')

# exercise 7
# Виведення поточного часу в мілісекундах
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)

print('-----')

# exercise 8
# Напишіть код для перетворення заданого об'єкта дати та часу в рядок.
from datetime import datetime
given_date_4 = datetime(2020, 2, 25)
string_date = given_date_4.strftime('%Y-%m-%d %H:%M:%S')
print(string_date)

print('-----')

# exercise 9
# Обчисліть дату через 4 місяці від поточної дати
# Нам потрібно використовувати dateutilмодуль  Python relativedelta. 
# Ми можемо додати 4 місяці до заданої дати, використовуючи метод 
# relativedelta.
# Це  relativedelta корисно, коли нам потрібно мати справу з місяцями 
# з 29, 30 та 31 днями. Це правильно налаштує дні
from datetime import datetime
from dateutil.relativedelta import relativedelta
# 2020-02-25
print('First date is: 2020-02-25')
given_date_5 = datetime(2020, 2, 25).date()
months_to_add = 4
new_date = given_date_5 + relativedelta(months=+ months_to_add)
print(new_date)

print('-----')

# exercise 10
# Напишіть код для обчислення кількості днів між двома датами
from datetime import datetime
date_1 = datetime(2020,2,25).date()
date_2 = datetime(2020, 9, 17).date()

delta = None
if date_1 > date_2:
    print('date_1 is greater.')
    delta = date_1 - date_2
else:
    print('date_2 is greater.')
    delta = date_2 - date_1
print(f'Difference is: {delta.days} days.')

