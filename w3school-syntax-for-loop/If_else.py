#exercise 1: poliandrom
text_1 = input("Enter Your string: ").replace(" ", "").lower()
if text_1 == text_1[::-1]:
    print("This string is poliandrom.")
else:
    print("This is not poliandrom.")

print("-" * 30)

#exercise 2: this number is prime?
m = int(input("Enter Your number: "))
is_prime = True
if m < 2:
    is_prime = False
else:
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            is_prime = False
            break
if is_prime:
    print("This number is prime.")
else:
    print("This number isn`t prime!")

print("-" * 30)

# exercise 3:
# temperature of water input
temperature = float(input("Введіть температуру води у °C: "))

# умовний оператор для визначення стану
if temperature < 0:
    print("Вода знаходиться у твердому стані.")
elif 0 <= temperature <= 100:
    print("Вода знаходиться у рідкому стані.")
else: # temperature > 100
    print("Вода знаходиться у стані пару.")

print("-" * 30)

# exercise 4:
# введення цілого числа
number = int(input("Введіть ціле число: "))

# умовний оператор для перевірки знака числа
if number > 0:
    print(f"Число {number} є позитивним.")
elif number < 0:
    print(f"Число {number} є негативним.")
else: # number == 0
    print(f"Число {number} є нулем.")

print("-" * 30)

#exercise 5:
total_amount = float(input("Введіть загальну суму покупки ($.): "))

# змінна для зберігання відсотку знижки
discount_percentage = 0.0

# умовний оператор для визначення розміру знижки
if total_amount < 1000:
    discount_percentage = 0.0
elif 1000 <= total_amount <= 5000:
    discount_percentage = 0.05  # 5%
else: # total_amount > 5000
    discount_percentage = 0.10  # 10%

# розрахунок суми знижки
discount_amount = total_amount * discount_percentage

# розрахунок підсумкової суми до сплати
final_amount = total_amount - discount_amount

# виведення результатів
print(f"Відсоток знижки: {discount_percentage * 100:.0f}%")
print(f"Сума знижки: {discount_amount:.2f} $.")
print(f"Підсумкова сума до сплати: {final_amount:.2f} $.")