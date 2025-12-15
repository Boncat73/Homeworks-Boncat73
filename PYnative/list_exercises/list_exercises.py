print("-" * 30)

my_list = ['trek', 'cannondale', 'redline', 'specialized']
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])
print(my_list[-4])
print(my_list[1:])
print(my_list[:3])
print(my_list[1:4])
print(my_list[1].title())
print(my_list[3].title())
print(my_list[2].capitalize())
print(my_list[-4].upper())
print(my_list[2].upper())
print(my_list[0].upper())

print("-" * 30)

my_son_list = ["Daniel", "George"]
print(f"Hello, my sons: {my_son_list}!")
print(f"Hello, {my_son_list[0]}!")
print(f"Hello, {my_son_list[1]}!")

print("-" * 30)

my_list_auto = ["audi", "merseder", "pego", "reno", "tesla"]
print(my_list_auto)
print(my_list_auto[0])
print(my_list_auto[1])
print(my_list_auto[2])
print(my_list_auto[3])
print(my_list_auto[4])
print(my_list_auto[0].upper())
print(my_list_auto[1].upper())
print(my_list_auto[2].upper())
print(my_list_auto[3].upper())
print(my_list_auto[4].upper())
print(f"I don`t like auto, but I would to buy: {my_list_auto[0]}.")
print(f"I did`t to buy an auto! And these: {my_list_auto}!")

print("-" * 30)

my_list_fruits = ["apple", "mango", "apricot", "banana", "orange"]
print(my_list_fruits) # print old list
my_list_fruits[1] = "HONDA" # change items in list
print(my_list_fruits) # print new list

# add item in list 
my_list_fruits.append("Ducatti")
print(my_list_fruits)
my_list_fruits.append("Honda")
my_list_fruits.append("Audi")
print(my_list_fruits)

print("-" * 30)

motorcycles = []
motorcycles.append("Honda") # add items
motorcycles.append("Yamaha")
motorcycles.append("Kawasaki")
print(motorcycles)

print("-" * 30)

motorcycles.insert(0, "Ducati")
print(motorcycles)
motorcycles.insert(1, "Java")
print(motorcycles)

print("-" * 30)

# remove item
things = ["chair", "table", "book", "lamp"]
print(things)
del things[0]
print(things)
del things[2]
print(things)

print("-" * 30)

# method pop()
my_list_auto = ["audi", "mersedes", "pego", "reno", "tesla"]
print(my_list_auto)
pop_my_list_auto = my_list_auto.pop()
print(my_list_auto)
# remove last item and return last item in variable pop_my_list_auto
print(pop_my_list_auto) 
my_list_auto.remove("mersedes")
print(my_list_auto)

print("-" * 30)

# exercises 1:
my_people = ["mother", "father", "brother 1", "brother 2", "son 1", "son 2"]
print(my_people)
print(f"Dear {my_people[-1]} come me in Friday at 7 p.m.")
print(f"Dear {my_people[-2]} come me in Friday at 7 p.m.")

print("-" * 30)

# exercise 2:
print(f"Dear {my_people[-2]} doesn`t come to me.")
my_people.append("friend 1")
my_people.append("friend 2")
print(f"Dear {my_people[-1]} come to me in Friday at 7 p.m.")
print(my_people)
print(f"List my people: \n{my_people[-1]} \n{my_people[-2]} \n{my_people[-3]}.")

print("-" * 30)

# exercise 3:
my_people = ["son 1", "son 2", "friend 1", "friend 2", "friend 3", "friend 4"]
my_people_dead = ["mother", "father", "brother 1", "brother 2",]
print(f"The people where could come to me in weekend:\n{my_people[0]}\n{my_people[1]}\n{my_people[2]}\n{my_people[3]}\n{my_people[4]}\n{my_people[5]}")
print(f"Dear {my_people[0]}, come to me in Friday at 7 p.m.")
print(f"Dear {my_people[1]}, come to me in Friday at 7 p.m.")
print(f"Dear {my_people[2]}, come to me in Friday at 7 p.m.")
print(f"Dear {my_people[3]}, come to me in Friday at 7 p.m.")
print(f"Dear {my_people[4]}, come to me in Friday at 7 p.m.")
print(f"Dear {my_people[5]}, come to me in Friday at 7 p.m.")

print("-" * 30)

# exercise 4:
print("Sorry, but I can invite only two people to dinner.")
while len(my_people) > 2:
    removed_person = my_people.pop()
    print(f"Dear {removed_person}, sorry but I can`t invite you to dinner.")
print(f"The people where could come to me in weekend:\n{my_people[0]}\n{my_people[1]}")
print(f"Dear {my_people[0]}, you are still invited to dinner.")
print(f"Dear {my_people[1]}, you are still invited to dinner.")

# empty list
del my_people[1]
del my_people[0]
print(my_people)    

print("-" * 30)

# exercise 5:
my_places = ["Italy", "Spain", "France", "Germany", "Greece"]
print(my_places)
print(sorted(my_places))
print(my_places)
my_places.reverse()
print(my_places)
my_places.reverse()
print(my_places)
my_places.sort()
print(my_places)
my_places.sort(reverse=True)
print(my_places)    

print("-" * 30)

# exercise 6: method sort()
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print("Here is the original list again:")
print(cars) 

print("-" * 30)

# exercise 7: len() function
my_countries = ["Ukraine", "Poland", "Germany", "Italy", "Spain"]
print(f"My list countries has {len(my_countries)} items.")  

print("-" * 30)

# exercise 8: fucntion sorted()
my_countries = ["Ukraine", "Poland", "Germany", "Italy", "Spain"]
print(my_countries)
print(sorted(my_countries))
print(my_countries)
my_countries.reverse()
print(my_countries)
my_countries.reverse()
print(my_countries)
my_countries.sort()
print(my_countries)
my_countries.sort(reverse=True)
print(my_countries) 

print("-" * 30)

# exercise 9:
numbers = [1, 8, 3, 10, 4, 7]

result_list = []
for number in numbers:
    squared = number ** 2
    result_list.append(squared)
print("Original list:", numbers)
print("Squared list:", result_list)

print("-" * 30)

# exercise 10:
numbers = [1, 8, 3, 10, 4, 7]

# створюємо порожній список
result_list = []

# перевіряємо послідовно кожне число
# 'num' — це тимчасове імʼя для перевірки
for num in numbers:

    # дивимось на число, воно більше 5?
    if num < 5:

        # якщо ТАК, кладемо у кошик
        # Метод .append() додає елемент у кінець списку
        result_list.append(num)

# друкуємо результат
print(result_list)

print("-" * 30)

# exercise 11:
numbers = [] # create empty list
if numbers == []:
    print("This list is empty.")
else:
    # сюди ми потрапимо, якщо список НЕ порожній
    current_min = [0]
    for number in numbers[1:]:
        if number < current_min:
            current_min = number
    print(f"The smallest number in this list is: {current_min}.")

print("-" * 30)

# exercise 11/1
# Створення списку за допомогою двох списків
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

print('-----')

# exercise 11/2
# Видалення та додавання елемента до списку
list1 = [54, 44, 27, 79, 91, 41]
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
# pop(index)Видаляє та повертає елемент за заданим індексом зі списку.
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)
# insert(index, item)Додати елемент у вказану позицію (індекс) у списку
sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)
# append(item)Додати елемент у кінець списку.
sample_list.append(element)
print("List after Adding element at last ", sample_list)

print('-----')

# exercise 11/3
# Розділіть список на 3 рівні частини та переверніть кожну частину
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)
# Отримати довжину списку за допомогою len()функції
length = len(sample_list)
# Поділіть довжину на 3, щоб отримати розмір шматка
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times Виконати цикл тричі
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    # У кожній ітерації отримати фрагмент за допомогою 
    # slice(start, end, step)функції та перевернути 
    # його за допомогою reversed()функції
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))
    # У кожній ітерації startзначення endзмінюватиметься
    start = end
    end += chunk_size

    print('-----')

# exercise 11/4
# Підрахуйте кількість входжень кожного елемента зі списку
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

print('-----')

# exercise 11/5
# створення набору Python таким чином, щоб він 
# відображав елементи з обох списків у парі.
first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

print('-----')

# exercise 11/6
# знаходження перетину (спільної точки) двох множин 
# та видалення цих елементів з першої множини
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)
# Отримайте поширені елементи за допомогою first_set.intersection(second_set)
intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
# У кожній ітерації використовуйте remove()метод on 
# first set та передайте йому поточний елемент.
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)

print('-----')

# exercise 11/7
# код для перевірки, чи є одна множина підмножиною або 
# надмножиною іншої множини. Якщо знайдено, видаліть 
# усі елементи з цієї множини.
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is Super set of second set - ", first_set.issuperset(second_set))
print("Second set is Super set of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

print('-----')

# exercise 11/8
# Напишіть програму для ітерації заданого списку та перевірки, 
# чи існує заданий елемент як значення ключа у словнику. 
# Якщо ні, видаліть його зі списку.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 
               'Emma': 69, 
               'Kelly': 76, 
               'Jason': 97
}

print("List:", roll_number)
print("Dictionary:", sample_dict)

# create new list
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print("after removing unwanted elements from list:", roll_number)

print('-----')

# exercise 11/9
# Вилучення унікальних значень зі словника для списку
speed = {'jan': 47, 
         'feb': 52, 
         'march': 47, 
         'April': 44, 
         'May': 52, 
         'June': 53,
         'july': 54, 
         'Aug': 44, 
         'Sept': 54
}

print("Dictionary's values - ", speed.values())

speed_list = list()

# iterate dict values
for val in speed.values():
    # check if value not present in a list
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)

print('-----')

# exercise 11/10
# видалення дублікатів зі списку
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sample_list)

sample_list = list(set(sample_list))
print("unique list", sample_list)

t = tuple(sample_list)
print("tuple ", t)

print("Minimum number is: ", min(t))
print("Maximum number is: ", max(t))