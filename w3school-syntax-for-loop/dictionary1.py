# Task 3:
# Початковий словник (використовуємо той, що був у Задачі 1)
student_info = {
    "ім'я": "Марія",
    "вік": 19,
    "курс": 2,
    "середній_бал": 4.8
}

# 1. Зміна значення
student_info["курс"] = 3

# 2. Додавання нового ключа
student_info["спеціальність"] = "Комп'ютерні науки"

# 3. Видалення ключа
del student_info["вік"]

# Виведення оновленого словника
print("Task 3:")
print("Оновлений словник:")
print(student_info)

print(" ")
# Task 4: ітерація та підрахунок у словнику
inventory = {
    "Apple": 50,
    "Bananas": 15,
    "Orange": 30,
    "Mango": 45
}

total_items = 0

print("Task 4:")
print("Товари на складі:")

# 1. Ітерація по елементах словника за допомогою циклу for
for item, quantity in inventory.items():
    print(f"Товар: {item.capitalize()}, Кількість: {quantity}")
    
    # 2. Підрахунок загальної кількості
    total_items += quantity

print("-" * 20)
print(f"Загальна кількість товарів на складі: {total_items}")

print(" ")

# Task 5: поєднання словника зі списком (аналіз даних)
# підрахувати загальну кількість успішних тестів
# знайти найвищий балл
dict_people = [
    {'name': 'Anna', 'age': 24, 'score': 92, 'passed': True},
    {'name': "Bogdan", 'age': 31, 'score': 78, 'passed': True},
    {'name': "Victor", 'age': 45, 'score': 65, 'passed': False},
    {'name': "Galina", 'age': 51, 'score': 95, 'passed': True},
    {'name': "Daniel", 'age': 23, 'score': 55, 'passed': False},
    {'name': "George", 'age': 20, 'score': 83, 'passed': True},
]

passed_count = 0 # змінна для підрахунку тих, хто пройшов
max_score = 0 # змінна для зберігання найвищого балу

# ітерація по списку словників
for student in dict_people:
    # підрахунок тих, хто пройшов
    if student['passed'] == True:
        passed_count += 1

    # знаходження найвищого балу
    current_score = student['score']
    if current_score > max_score:
        max_score = current_score

# виведення результатів
print("Task 5:")
print(f"Загальна кількість студентів: {len(dict_people)}")
print(f"Кількість студентів, які успішно склали тест: {passed_count}")
print(f"Найвищий набраний бал: {max_score}")


# Task 6:
# Визначити середню зарплату у кожному відділі.
# Визначити найвищу зарплату по всій компанії та ім'я співробітника, який її отримує.
# Вивести результати.

company_data = {
    "HR": {
        "Олена": 40000,
        "Сергій": 35000
    },
    "Розробка": {
        "Іван": 80000,
        "Марія": 95000,
        "Петро": 75000
    },
    "Продажі": {
        "Наталя": 60000
    }
}

# Змінні для пошуку максимальної зарплати
max_salary = 0
top_earner_name = ""
top_earner_dept = ""

# 1. Ітерація по відділах (зовнішній словник)
for department, employees in company_data.items():
    # department - назва відділу ('HR', 'Розробка', 'Продажі')
    # employees - словник зі співробітниками та зарплатами цього відділу

    total_dept_salary = 0
    num_employees = 0

    # 2. Ітерація по співробітниках відділу (внутрішній словник)
    for name, salary in employees.items():
        total_dept_salary += salary
        num_employees += 1

        # 3. Перевірка максимальної зарплати по всій компанії
        if salary > max_salary:
            max_salary = salary
            top_earner_name = name
            top_earner_dept = department
            
    # Обчислення середньої зарплати відділу
    if num_employees > 0:
        average_salary = total_dept_salary / num_employees
        print(f"Відділ **{department}**:")
        print(f"  Середня зарплата: {average_salary:,.2f} грн.")
    else:
        print(f"Відділ {department}: Немає співробітників.")

print("Task 6:")
print("-" * 35)
print(f"Найвища зарплата по компанії ({max_salary:,.2f} грн.) належить:")
print(f"  Співробітник: **{top_earner_name}** ({top_earner_dept})")