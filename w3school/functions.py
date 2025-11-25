# task 1
# створіть функцію, яка приймає два аргументи: ім'я та рік народження.
# функція повинна вирахувати вік людини на основі поточного року (2025)
# та повернути рядок у форматі: "Привіт, [ім'я]! Тобі [вік] років."

def greet_user(name, birth_year):
    # поточний рік
    current_year = 2025
    age = current_year - birth_year

    # повертаємо форматований рядок
    return (f"Hello, {name}! You are {age} years old.")
# приклади виклику функції
message = greet_user("Daniel", 2002)
print(message)

print("-----")

# task 2
# створіть функцію, яка приймахє два обовʼязкові аргументи та один
# необовʼязковий аргумент 
def add_numbers(a, b, c = 0):
    total = a + b + c 
    return total 
# виклик з двома обовʼязковими аргументами (с = 0 за замовчуванням)
result_1 = add_numbers(5, 10)
print(f"5 + 10 = {result_1}")

# виклик з трьома аргументами
result_2 = add_numbers(5, 10, 2)
print(f"5 + 10 + 2 = {result_2}")

print("-----")

# task 3
# створіть функцію, яка приймає строку, рахує та повертає одночасно
# два значення: кількість символів у рядку та кількість слів у рядку
def analize_text(text):
    # кількість символів
    char_count = len(text)

    # метод .split() розбиває рядок на слова за пробілами
    word_list = text.split()
    word_count = len(word_list)

    # повертаємо обидва значення як кортеж (автоматичне пакування)
    return char_count, word_count

# приклад виклику функції
text_to_analyze = "Hello, World! This is a sample text."
length, words = analize_text(text_to_analyze)

print(f"Length of text: {length} characters")
print(f"Number of words: {words}")

