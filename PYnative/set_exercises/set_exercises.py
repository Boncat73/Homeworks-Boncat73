# exercise 1
# Виконання основних операцій з множинами
# 1. Create a Set
fruits = {"apple", "banana", "mango", "orange"}
print("1. After creating the set:", fruits)

# 2. Add Element
fruits.add("grape")
print("2. After adding 'grape':", fruits)

# 3. Remove Element
fruits.remove("banana")
print("3. After removing 'banana':", fruits)

# 4. Discard Element
fruits.discard("mango")
print("4. After discarding 'mango':", fruits)

print('-----')

# exercise 2
# Об'єднання множин
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

print('-----')

# exercise 3
# Знайдіть перетин set1та set2. Напишіть код, який 
# повертає нову множину, що містить лише елементи, 
# спільні для та set1.set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

print('-----')

# exercise 4
# Знайдіть різницю ( set1 - set2). Напишіть код, який 
# повертає новий набір, що містить елементи, які присутні 
# в , set1але відсутні в set2.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
difference_set = set1.difference(set2)
print("3. Difference (set1 - set2):", difference_set)

print('-----')

# exercise 5
# Знайдіть симетричну різницю set1та set2. Напишіть код, 
# який повертає новий набір, що містить елементи, унікальні 
# для одного з set1або set2, але не в обох. Це як знайти 
# об'єднання, а потім видалити перетин.
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

print('-----')

# exercise 6
# Додавання списку елементів до множини
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

print('-----')

# exercise 7
# оновлення першого набору лише тими елементами, 
# які є унікальними для нього (тобто відсутніми 
# в другому наборі)
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

print('-----')

# exercise 8
# Напишіть програму на Python, яка одночасно 
# видаляє елементи 10, 20, 30 з наступного набору
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

print('-----')

# exercise 9
# Перевірте, чи set1є підмножиною set2. Напишіть код, 
# який поверне результат, Trueякщо кожен елемент у 
# subset_setтакож присутній у main_set
# 1. Check Subset
subset_set = {10, 20}
main_set = {10, 20, 30, 40}

is_subset = subset_set.issubset(main_set)
print(f"Is {subset_set} a subset of {main_set}? {is_subset}")

print('-----')

# exercise 10
# Перевірте, чи main_set = {10, 20, 30, 40}є надмножиною subset_set = {10, 20}
subset_set = {10, 20}
main_set = {10, 20, 30, 40}
is_superset = main_set.issuperset(subset_set)
print(f"Is {main_set} a superset of {subset_set}? {is_superset}")

print('-----')

# exercise 11 
# Напишіть код, який перевіряє, чи мають дві множини 
# спільні елементи. Якщо так, виведіть спільні елементи
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))

print('-----')

# exercise 12
# Напишіть програму для оновлення set1шляхом додавання 
# елементів з множин set2, які не є спільними для обох множин
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

print('-----')

# exercise 13
# Напишіть код для видалення елементів з set1, 
# яких немає вset2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)

print('-----')

# exercise 14
# Знайдіть спільні елементи у двох списках
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

set_list1 = set(list1)
set_list2 = set(list2)

common_elements = set_list1.intersection(set_list2)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements using sets: {common_elements}")

print('-----')

# exercise 15
# Створити заморожений набір зі списку
my_list = [10, 20, 30]
frozen_set = frozenset(my_list)
print(f"Original list: {my_list}")
print(f"Created frozen set: {frozen_set}")

print('-----')

# exercise 16
# Підрахунок унікальних слів
sentence = "dog is a simple animal dogs is selfless animal"

# Convert the sentence to lowercase and split it into words
words = sentence.lower().split()

# Convert the list of words to a set to get unique words
unique_words = set(words)

# Count the number of unique words
unique_word_count = len(unique_words)

print(f"Original sentence: '{sentence}'")
print(f"Number of unique words: {unique_word_count}")