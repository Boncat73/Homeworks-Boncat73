# exercise 2
# Напишіть програму для створення функції func1(), яка приймає 
#змінну кількість аргументів та виводить кожне з їхніх значень.
# Примітка: Створіть цю функцію так, щоб вона могла отримувати 
# будь-яку кількість аргументів, обробляти їх та відображати 
# значення кожного окремого аргументу.
def func1(*agrs):
    for arg in agrs:
        print(arg)

func1(1, 2, 3)
func1(3, 6, 2)

print("-----")

def func2(*numbers):
    print("Printing values:")
    for number in numbers:
        print(number)

func2(10, 20, 30, 40)

print("-----")

# exercise 3
# Напишіть функцію calculation(), яка приймає дві змінні та обчислює 
# як їх додавання, так і віднімання. Функція повинна потім повертати 
# як суму, так і різницю в одному операторі return.
def calculation(num1, num2):
    addition = num1 + num2
    substraction = num1 - num2
    print(addition, substraction)

calculation(45, 12)

print("-----")

# exercise 4
# Напишіть програму для створення функції show_employee() з такими специфікаціями:
# Вона повинна приймати ім'я та зарплату співробітника.
# Вона повинна відображати як ім'я, так і зарплату.
# Якщо зарплата не вказана у виклику функції, вона повинна за замовчуванням дорівнювати 9000.
def show_employee(name, salary = 9000):
    print(f"Employee Name: {name}, Salary: {salary}")   

show_employee("Ben", 12000)
show_employee("Jessa")

print("-----")

# exercise 5
# Створіть програму з вкладеними функціями для виконання обчислення 
# додавання наступним чином:
# Bизначте зовнішню функцію, яка приймає два параметри, a та b.
# Усередині цієї зовнішньої функції визначте внутрішню функцію, яка обчислює суму a та b.
# Зовнішня функція повинна додати 5 до цієї суми.
# Нарешті, зовнішня функція повинна повернути результуюче значення.
def outer_function(a, b):
    def inner_function():
        return a + b
    result = inner_function() + 5
    return result

print(outer_function(10, 15))


print("-----")

# exercise 6
# Напишіть програму для створення рекурсивної функції, 
# яка обчислює суму чисел від 0 до 10.
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
    
print(recursive_sum(10))

print("-----")

# exercise 7
# Нижче наведено функцію display_student(ім'я, вік). Призначте їй 
# нове ім'я show_student(ім'я, вік) та викличте її, використовуючи нове ім'я.
def display_student(name, age):
    print(name, age)

display_student("Sarah", 22) # виклик функції за оригінальним іменем

show_student = display_student # присвоєння нового імені функції

show_student("Daniel", 25) # виклик функції за новим іменем

print("-----")

# exercise 8
# Очікуваний результат:
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
def generate_even_numbers(n):        # функція для генерації списку парних чисел до n * 2
    even_numbers = []                # створення порожнього списку для збереження парних чисел
    for i in range(2, n * 2 + 1, 2): # iтерування від 2 до  n * 2 з кроком 2
        even_numbers.append(i)       # додавання парного числа до списку
    return even_numbers              # повернення списку парних чисел 

print(generate_even_numbers(14))

print("-----")

def func1(n):
    print(list(range(2, 30, 2))) # альтернативний спосіб

func1(14)

print("-----")

# exercise 9
# Знайдіть найбільший елемент зі списку
x = [4, 6, 8, 24, 12, 2]
print(max(x)) # вбудована функція max() !!!

def find_maximum(numbers):
    maximum_number = numbers[0] # припускаємо, що перший елемент є найбільшим
    for number in numbers: # ітеруємося по кожному числу в списку
        if number > maximum_number: # якщо поточне число більше за maximum_number
            maximum_number = number # оновлюємо maximum_number
    return maximum_number # повертаємо найбільше число

print(find_maximum(x))

print("-----")

# exercise 10
# Визначте функцію describe_pet(animal_type, pet_name), яка виводить опис
# домашньої тварини. Викличте цю функцію, використовуючи як позиційні, так 
# і ключові аргументи.
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}.")

describe_pet('hamster', 'Harry') # виклик функції з позиційними аргументами
describe_pet('dog', 'Lucy') # виклик функції з позиційними аргументами

describe_pet(animal_type="cat", pet_name="Misty") # виклик функції з ключовими аргументами
describe_pet(pet_name="Buddy", animal_type="dog") # виклик функції з ключовими аргументами у довільному порядку

print("-----")

# exercise 11
# Створіть функцію print_info(**kwargs), яка приймає ключові слова як 
# аргументи та друкує пари ключ-значення. Викличте її з різними ключовими 
# словами як аргументами.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name = "Alice", age = 30, city = "New York")
print_info(product = "Laptop", price = 1200, brand = "Dell", stock = 25)


# # другий варіант
def print_info(**kwargs):
    if kwargs: # перевірка, чи є передані аргументи
        print("\nProvided key-value pairs:") # заголовок перед виведенням пар ключ-значення
        for key, value in kwargs.items():
            print(f"{key}: {value}")

print_info(name = "Alice", age = 30, city = "New York")
print_info(product = "Laptop", price = 1200, brand = "Dell", stock = 25)

print("-----")

# exercise 12
# Визначте глобальну змінну global_var = 10. Напишіть функцію, яка 
# змінює значення глобальної змінної.
global_var = 10
def modify_global():
    global global_var # оголошення глобальної змінної для зміни її значення всередині функції
    global_var = 20 # зміна значення глобальної змінної
    print("Inside function:", global_var)

modify_global() # виклик функції для зміни глобальної змінної
print("Before modification:", global_var)

print("-----")

# exercise 13
# Напишіть рекурсивну функцію для обчислення факторіала невід'ємного цілого числа.
def factorial_rec(n):
    if n == 0 or n == 1: # базовий випадок: факторіал 0 або 1 дорівнює 1
        return 1
    else:
        return n * factorial_rec(n - 1) # рекурсивний випадок
    
print(factorial_rec(5)) # приклад виклику функції для обчислення факторіала числа 5

# другий варіант
def factorial_rec(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1 # базовий випадок: факторіал 0 дорівнює 1
    else:
        return n * factorial_rec(n - 1) # рекурсивний випадок
    
number = 5
result = factorial_rec(number)
print(f"The factorial of {number} is {result}.")

print("-----")

# exercise 14
# Створіть лямбда-функцію, яка підносить задане число до квадрата
square = lambda x: x ** 2

number = 5
squared_number = square(number)
print(f'The square of {number} is {squared_number}')

print('-----')

# exercise 15
# Використання лямбда-виразу з filter()функцією для 
# отримання всіх парних чисел зі списку
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f'The even numbers in the list are: {even_numbers}')

print('-----')

# exercise 16
# Використання лямбда-виразу з map()функцією для 
# подвоєння кожного елемента у списку
numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x * 2, numbers))
print(f'The doubled numbers are: {doubled_numbers}')

print('-----')

# exercise 17
# Використання лямбда-виразу з sorted()функцією 
# для сортування списку кортежів на основі другого елемента
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]

sorted_data = sorted(data, key = lambda item: item[1])
print(f'The sorted list of tuples based on the second element is: {sorted_data}')

# exercise 18
# Створення функції вищого порядку
def apply_operation(func, x, y):
    # Applies a given function to two numbers
    # Args:
    #   func: the function to apply (should take two arguments)
    #   x: the first number
    #   y: the second number
    # Returns:
    #   the result of calling func(x, y)
    return func(x, y)

# demonstrate with addition using a regular function
def add(a, b):
    return a + b

result_add = apply_operation(add, 5, 3)
print(f'Result of addition: {result_add}')

# demonstrate with subtraction using a lambda function
subtract = lambda a, b: a - b
result_subtract = apply_operation(subtract, 10, 4)
print(f'Result of subtraction: {result_subtract}')

# demonstrate with multiplication using another lambda function
multiply = lambda a, b: a * b
reult_multiply = apply_operation(multiply, 2, 6)
print(f'Result of multiplication: {reult_multiply}')

