# Список — це впорядкована та змінна колекція. Дозволяє дублікати членів.
# Кортеж — це впорядкована та незмінна колекція. Дозволяє дублікати членів.
# Set — це невпорядкована, незмінна та неіндексована колекція. Без дублікатів членів.
# Словник — це впорядкована та змінна колекція. Дублікати членів відсутні.

# tuple
thistuple = ("apple", "mango", "banana")
print(thistuple)
print(type(thistuple))
print(len(thistuple))
print(thistuple[0])
print(thistuple[1])
print(thistuple[2])
print(thistuple[-1])
print(thistuple[-2])
print(thistuple[-3])

print("-" * 30)

thistuple_1 = ("apple", "mango", "banana", "apricot", "mango", "potato")
print(thistuple_1)
print(len(thistuple_1))
print(type(thistuple_1))

print("-" * 30)

thistuple_2 = ("mango",)
print(type(thistuple_2))
print(thistuple_2)

print("-" * 30)

my_tuple = (24, "True", False, "String")
print(type(my_tuple))
print(my_tuple)

print("-" * 30)

tuple_1 = (1, 2, 3, 4, 5)
tuple_2 = (False, True, True, True, False)
tuple_3 = ("apple", "mango", "apricot")
print(tuple_1, tuple_2, tuple_3)

print("-" * 30)
# Кортежі дозволяють дублікати значень.

fruits_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits_tuple[2:5])
print(fruits_tuple[:4])
print(fruits_tuple[2:])
print(fruits_tuple[-1:-4])
if "apple" in fruits_tuple:
    print("Yes, 'apple' is in the fruits tuple." )
else:
    print("NO! It is not!")

print("-" * 30)

# Після створення кортежу його значення не можна змінити. Кортежі є 
# незмінними або незмінними , як їх ще називають.
# Але є обхідний шлях. Ви можете перетворити кортеж на список, 
# змінити список і перетворити список назад на кортеж.
fruits = ("apple", "banana", "cherry")
fruits_in_list = list(fruits)
fruits_in_list[1] = "apricot"
fruits = tuple(fruits_in_list)
print(fruits)

print("-" * 30)  

# Оскільки кортежі незмінні, вони не мають вбудованого append()методу,
# але існують інші способи додавання елементів до кортежу:
# Перетворення на список : Як і у випадку зі зміною кортежу, 
# ви можете перетворити його на список, додати елементи та 
# перетворити їх назад на кортеж.
fruits = ("apple", "banana", "cherry")
fruits_in_list = list(fruits)
fruits_in_list.append("orange")
fruits = tuple(fruits_in_list)
print(fruits)
