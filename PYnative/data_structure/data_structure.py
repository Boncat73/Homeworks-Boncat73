# exercise 1
# Створення списку за допомогою двох списків
list_1 = [3, 6, 9, 12, 15, 18, 21]
list_2 = [4, 8, 12, 16, 20, 24, 28]

list_3_odd = list_1[1::2]
print(f'Element at odd-index positions from list one {list_3_odd}')
list_4_even = list_2[0::2]
list_ = list_3_odd + list_4_even
print(f'Element at even-index positions from list two {list_4_even}')
print(f'Printing result {list_3_odd}, {list_4_even}.')
print(list_)

print('-----')

# exercise 2
# Видалення та додавання елемента до списку
# Напишіть програму для видалення елемента, присутнього 
# в індексі 4, та додавання його на 2-гу позицію та в кінець списку
list_5 = [54, 44, 27, 79, 91, 41]
print('Original list ', list_5)
element = list_5.pop(4)
print('List after removing element at index 4 ', list_5)

list_5.insert(2, element)
print('List after adding element at index 2 ', list_5)

list_5.append(element)
print('List after adding element at last ', list_5)

print('-----')

# exercise 3
# Розділіть список на 3 рівні частини та переверніть кожну частину
list_6 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print(f'Original list: {list_6}')

length = len(list_6)
size_on_three = int(length / 3)
start = 0
end = size_on_three

for i in range(1, 4): # Починаємо з 1 для гарного виводу "Size 1, 2, 3"
    # Отримуємо зріз (slice)
    indexes = slice(start, end)
    
    # Отримуємо частину списку
    current_chunk = list_6[indexes]
    print(f'Chunk {i}: {current_chunk}')

    # Перевертаємо та виводимо
    reversed_chunk = list(reversed(current_chunk))
    print(f'After reversing it: {reversed_chunk}')

    # Оновлюємо індекси для наступної ітерації
    start = end
    end += size_on_three # Додаємо число (крок), а не список!

    print('-----')

    # exercise 4
    # Підрахуйте кількість входжень кожного елемента зі списку
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    print('Original list ', sample_list)
    count_dict = dict()
    for item in sample_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
print('Printing count of each item ', count_dict)

print('-----')

# exercise 5
# Напишіть код для створення набору Python таким чином, 
# щоб він відображав елементи з обох списків у парі
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

print(f'First list: {first_list}')
print(f'Second list: {second_list}')

result = zip(first_list, second_list)
relult_set = set(result)
print(relult_set)

print('-----')

# exercise 6
# Напишіть код для знаходження перетину (спільної точки) 
# двох множин та видалення цих елементів з першої множини
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print(f'First Set {first_set}')
print(f'Second Set {second_set}')

# Отримайте поширені елементи
intersection = first_set.intersection(second_set)
print(f'Intersection is {intersection}')

# ітеруємо загальні елементи за допомогою циклу for використовуємо 
# remove()метод on first set та передайте йому поточний елемент
for item in intersection:
    first_set.remove(item)

print(f'First Set after removing common element {first_set}')

print('-----')

# exercise 7
# Напишіть код для перевірки, чи є одна множина підмножиною або 
# надмножиною іншої множини. Якщо знайдено, видаліть усі 
# елементи з цієї множини
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print(f'First Set: {first_set}')
print(f'Second Set: {second_set}')

print(f'Перша множина є підмножиною другої множини - {first_set.issubset(second_set)}')
print(f'Друга множина є підмножиною першої множини - {second_set.issubset(first_set)}')

print(f'Перший сет - це суперсет другого сету - {first_set.issuperset(second_set)}')
print(f'Другий сет - це суперсет першого сету - {second_set.issuperset(first_set)}')

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print(f'First Set: {first_set}')
print(f'Second Set: {second_set}')

print('-----')

# exercise 8
# Фільтрування списку за значеннями словника
# програму для ітерації заданого списку та перевірки, 
# чи існує заданий елемент як значення ключа у словнику. 
# Якщо ні, видаліть його зі списку
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print(f'List: {roll_number}')
print(f'Dictionary: {sample_dict}')

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print(f'After removing unwanted elements from list: {roll_number}')

print('-----')

# exercise 9
# Вилучення унікальних значень зі словника для списку
# Напишіть код, щоб отримати всі значення зі словника 
# та додати їх до списку, але не додавати дублікати
speed = {
    'jan': 47, 
    'feb': 52, 
    'march': 47, 
    'April': 44, 
    'May': 52, 
    'June': 53, 
    'july': 54, 
    'Aug': 44, 
    'Sept': 54
}

print(f'Dictionary`s values - {speed}')
speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print(f'Unique list: {speed_list}')

print('-----')

# exercise 10
# Напишіть код для видалення дублікатів зі списку, 
# створення кортежу та знаходження мінімальної 
# та максимальної кількості
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

print(f'Original list: {sample_list}')

sample_list = list(set(sample_list))
print(f'Unique list: {sample_list}')

t = tuple(sample_list)
print(f'Tuple: {t}')

print(f'Minimum number is: {min(t)}')
print(f'Maximum number is: {max(t)}')

