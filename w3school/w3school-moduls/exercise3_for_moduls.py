# exercise 3
# Використання from ... import ... та псевдонімів (as).
# 1. Імпорт лише однієї функції: randint
from random import randint

# 2. Імпорт модуля з псевдонімом: statistics як st
import statistics as st

# 3. Використовуємо randint без префікса модуля (бо імпортували напряму)
random_number = randint(1, 100)

# 4. Використовуємо функцію st.mean() (з псевдонімом)
data = [10, 20, 30]
average = st.mean(data)

# 5. Виводимо результати
print(f"Random a number for 1 to 100: {random_number}.")
print(f'List of numbers: {data}.')
print(f'Average value: {average}.')

print('-----')