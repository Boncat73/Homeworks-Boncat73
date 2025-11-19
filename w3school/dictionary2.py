# creat and modification ditionary
# 1. Створення початкового словника
student_scores = {
    'Anna': 92,
    'Borys': 78,
    'Taras': 85
}

print(f"Початковий словник: {student_scores}")

# 2. Додавання нового студента
student_scores['Darya'] = 95
print(f"Словник після додавання Darya: {student_scores}")

# 3. Оновлення балу студента Borys
student_scores['Borys'] = 88
print(f"Словник після оновлення балу Borys: {student_scores}")

# 4. Видалення студента Taras
del student_scores['Taras']
# Або можна використати: student_scores.pop('Taras')
print(f"Словник після видалення Taras: {student_scores}")

# 5. Виведення фінального словника
print(f"\n Фінальний словник: {student_scores}")

print("-" * 30)

# iteration and data mining
inventory = {
    'apples': 50,
    'bananas': 25,
    'oranges': 100,
    'kiwis': 15,
    'grapes': 75
}

# 1. Функція для пошуку товарів з низьким запасом
def get_low_stock_items(inventory_dict):
    low_stock_list = []
    # Ітерація по парах ключ-значення
    for item, quantity in inventory_dict.items():
        if quantity < 30:
            low_stock_list.append(item)
    return low_stock_list

# 2. Виведення списку
low_stock = get_low_stock_items(inventory)
print(f"Товари на складі менше 30 одиниць: {low_stock}") # ['bananas', 'kiwis']

# 3. Підрахунок загальної кількості всіх товарів
total_quantity = sum(inventory.values())

print(f"Загальна кількість усіх товарів: {total_quantity}") # 265

print("-" * 30)

# nested dictionaries and aggregation
project_progress = {
    'Olena': {'Project A': 60, 'Project B': 90},
    'Petro': {'Project A': 80, 'Project C': 50},
    'Mykola': {'Project B': 100, 'Project C': 70, 'Project D': 20}
}

# 1. Обчислення середнього відсотка завершення для кожного співробітника
print("\nСередній відсоток завершення проектів:")
for employee, projects in project_progress.items():
    # Отримуємо список всіх відсотків для даного співробітника
    scores = projects.values()
    
    # Обчислюємо середнє: сума / кількість проектів
    if scores: # Перевірка, щоб уникнути ділення на нуль, якщо projects пустий
        average_score = sum(scores) / len(scores)
        print(f"{employee}: {average_score:.2f}%")
    else:
        print(f"{employee}: Немає активних проектів")
        
# 2. Створення нового словника project_contributors
project_contributors = {}

# Ітерація по співробітниках і їхніх проектах
for employee, projects in project_progress.items():
    # Ітерація по проектах, над якими працює співробітник
    for project_name in projects.keys():
        
        # Використовуємо метод .setdefault(): 
        # Якщо ключ project_name ще не існує, він створюється зі значенням [],
        # інакше повертається існуючий список.
        project_contributors.setdefault(project_name, []).append(employee)
        
        # Альтернативний спосіб без setdefault:
        # if project_name not in project_contributors:
        #     project_contributors[project_name] = []
        # project_contributors[project_name].append(employee)


# 3. Виведення словника project_contributors
print("\n Учасники проектів:")
print(project_contributors)
# Очікуваний результат: 
# {'Project A': ['Olena', 'Petro'], 'Project B': ['Olena', 'Mykola'], 'Project C': ['Petro', 'Mykola'], 'Project D': ['Mykola']}