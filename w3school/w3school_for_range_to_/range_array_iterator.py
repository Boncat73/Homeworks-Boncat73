# range:
# знаходження суми усіх парних чисел від 1 до 100(включно)
sum_of_evens = 0
for number in range(2, 101, 2):
    sum_of_evens += number
print(f"Sum even numbers for 1 to 100: {sum_of_evens}.")


# друк чисел від 10 до 1 у зворотньому порядку
for i in range(10, 0, -1):
    print(i)
print('Start!')


# ітерація по індексам списка та друк кожного елемента
# разом з його індексом
fruits = ['apple', 'banana', 'cherry', 'apricot', 'kivi']
for index in range(len(fruits)):
    fruit_name = fruits[index]
    print(f"Index {index}: {fruit_name}.")

# arrays:
# знайти та надрукувати максимальний елемент у 
# списку чисел без вбудованої функції max()
numbers = [45, 12, 89, 5, 67, 34]
max_element = numbers[0]
for number in numbers[1:]:
    if number > max_element:
        max_element = number
print(f'List: {numbers}.')
print(f'Max element: {max_element}.')

# створити функцію,яка приймає список у якості аргумента
# та повертає новий список,у якому ці ж елементи у зворотньому
# порядку без вбудованих функцій срезів та reverse()
def reverse_array(input_list):
    reversed_list = []
    for i in range(len(input_list) -1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list
original_list = ['A', 'B', 'C', 'D', 'E']
result_list = reverse_array(original_list)
print(f'List: {original_list}.')
print(f'Reverse list: {result_list}.')

# підрахунок кількості унікальних елементів та друк 
# результату у вигляді пар (елемент,кількість)
data_list = [1, 2, 2, 3, 1, 4, 2, 3, 3, 1]
frequency = {}
for item in data_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print(f'List: {data_list}.')
print(f'Частота елементів: ')
for item, count in frequency.items():
    print(f'Елемент {item} зустрічається {count} раз(и)(ів).')

# iterators:
# 
#
#
#
#
#