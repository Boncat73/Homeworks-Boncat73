print("-" * 30)

# спільні інтереси
# створюємо списки інтересів
sports_person_A = ["soccer", "tennis", "basketball", "swimming"]
sports_person_B = ["basketball", "hokey", "swimming", "run", "boks"]

# перетворюємо списки на множини
set_A = set(sports_person_A)
set_B = set(sports_person_B)

# виконуємо оперцію перетину (&)
common_sports = set_A & set_B

print(f"Спільні види спорту: {common_sports}")

print("-" * 30)

# унікальні предмети
# використовуємо операцію обʼєднання,щоб знайти всі унікальні предмети за два семестри
semester_1 = {"Математика", "Історія", "Програмування", "Фізика", "Програмування"}
semester_2 = {"Хімія", "Математика", "Література", "Фізика"}
# множина (set) semester_1 автоматично видалила дублікат "Програмування"

# поєднуємо обидві множини
all_unique_subjects = semester_1 | semester_2

#
total_count = len(all_unique_subjects)

print(f"Усі унікальні предмети: {all_unique_subjects}.")
print(f"Загальна кількість унікальних предметів: {total_count}.")

print("-" * 30)

# відсутні товари (різниця)
# використовуємо операцію різниці (оператор - або difference)
all_products = {"A101", "B202", "C303", "D404", "E505"}
remaining_stock = {"A101", "D404", "F606", "C303"}

# Товари, які були продані (були в 'all_products', але відсутні в 'remaining_stock')
sold_products = all_products - remaining_stock
# Або: sold_products = all_products.difference(remaining_stock)

# Нові/помилкові товари (були в 'remaining_stock', але відсутні в 'all_products')
new_or_error_products = remaining_stock - all_products
# Або: new_or_error_products = remaining_stock.difference(all_products)
#

print(f"Продані товари (були, але зникли): {sold_products}.")
print(f"Нові/помилкові товари (зʼявилися, але не були в обліку): {new_or_error_products}.")
