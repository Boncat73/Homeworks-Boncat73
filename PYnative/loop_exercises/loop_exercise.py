# exercise 1
# print first 10 natural numbers using while loop
x = 1
while x <= 10:
    print(x)
    x += 1

print('-----')

# exercise 2
# write a Python code to print the following number pattern using a loop
print('Number Pattern')
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

print('-----')

# exercise 3
# wrute a Python prigram to accept a number from a user 
# and calculate the sum of all numbers from 1 to a given number

# version 1
s = 0 # store sum of all numbers
n = int(input('Enter your number: '))
# run a loop n times
# stop: n + 1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print('/n')
print('Sum is: ', s)

# version 2
n = int(input('Enter your number: '))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is: ', x)

# exercise 4
# print multiplication table of a given number
num = 2
# stop 11 (because range never include stop number in result)
# run loop 10 items
for i in range(1, 11, 1):
    result = n * i
    print(result)

print('-----')

# exercise 5
# write a Python program to display only those numbers from a list
# that satisfy the following conditions
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 ==0:
        print(item)

# exercise 6
# write a Python program to count the total number 
# of digits in a number using a while loop
num = 75869
count = 0
while num != 0:
    # floor division to reduce the last digit from number
    num = num // 10
    # increment counter by 1
    count = count + 1
print('Total digits are: ', count)

print('-----')

# exercise 7
# write a Python program to print the reverse 
# number pattern using a for loop
num1 = 5
num2 = 5
for i in range(0, num1 + 1):
    for j in range(num2 - i, 0, -1):
        print(j, end=' ')
    print()

print('-----')

# exercise 8
# print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
# version 1
# reverse list
new_list = reversed(list1)
# itarate reversed list
for item in new_list:
    print(item)

# version 2
# get list size len(list1) -1: because index start with 0
# iterate list in reverse order
# star from last item to first
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])

print('-----')

# exercise 9
# display number from -10 to -1 using for loop
for num in range(-10, 0, 1):
    print(num)

print('-----')

# exercise 10
# displayl a message 'Done' after the successful execution of the for loop
for i in range(5):
    print(i)
else:
    print('Done!')

print('-----')

# exercise 11
# Вивести всі прості числа в діапазоні 
start = 25
end = 50
print('Prime numbers between', start, 'and', end, 'are')
for num in range(start, end + 1):
    # all prime numbers are reater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop
                # and look for next number
                break
        else:
            print(num)

print('-----')

# exercise 12
# Відображення ряду Фібоначчі до 10 членів
num3, num4 = 0, 1
print('Fibonacci sequence: ')
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num3, end=" ")
    # add last two numbers to get next number
    res = num3 + num4
    # update values
    num3 = num4
    num4 = res

print('\n-----')

# exercise 13
# Знайти факторіал заданого числа
# Напишіть програму на Python, яка використовуватиме цикл
# for для знаходження факторіала заданого числа
num_fact = 5
factorial = 1
if num_fact < 0:
    print('Factorial does not exist for negative numbers')
elif num_fact == 0:
    print('The factorial of 0 is 1')
else:
    # run loop 5 items
    for i in range(1, num_fact + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print('The factorial of', num, 'is', factorial)

print('-----')

# exercise 14
# Зворотне ціле число
num6 = 76542
reverse_number = 0
print('Given number: ', num6)

while num6 > 0:
    # 1. Знаходимо останню цифру (залишок від ділення на 10)
    reminder = num6 % 10
    
    # 2. Оновлюємо обернене число:
    # Множимо поточне 'reverse_number' на 10 (зсуваємо цифри вліво)
    # та додаємо останню цифру 'reminder'
    reverse_number = (reverse_number * 10) + reminder
    
    # 3. Видаляємо останню цифру з вихідного числа (цілочисельне ділення на 10)
    num6 = num6 // 10

print('Reverse number: ', reverse_number)
# Вивід: Reverse number: 24567

print('-----')

# exercise 15
# Вивести елементи з заданого списку, присутні на 
# непарних позиціях індексу
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")

print('\n-----')

# exercise 16
# Обчисліть куб усіх чисел від 1 до заданого числа
imput_number = 6
for i in range(1, imput_number + 1):
    print('Current number is: ', i, ' and the cube is: ', (i * i * i))

print('-----')

# exercise 17
# Знайдіть суму ряду чисел до n членів
# number of terms
num7 = 2
terms = 5
sum_seq = 0
# run loop n times
for i in range(0, terms):
    print(num7, end="+")
    sum_seq += num7
    # calculate the next term
    num7 = num7 * 10 + 2
print('\nSum of above series is: ', sum_seq)

print('-----')

# exercise 18
# програмa для виведення шаблону за допомогою циклу for
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print('*', end=' ')
    print('\r')

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print('*', end=' ')
    print('\r')

print('-----')

# exercise 19
# код для генерації повної таблиці множення чисел від 1 до 10
# full multiplication table from 1 to 10
for i in range(1, 11):
    print('Multiplication table of: ', i)
    for j in range(1, 11):
        print(f' {i * j}', end='')
    print() # move to the next line after each row

print('-----')

# exercise 20
# Роздрукуйте шаблон альтернативних чисел
def print_alternate_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        if i % 2 != 0: # Непарний ряд: порядок зростання
            for x in range(num, num + i):
              print(x, end=' ')
            print() # відобразити наступний рядок числа на новому рядку
        else: # Парний ряд: у порядку спадання
            for y in range(num + i - 1, num - 1, -1):
              print(y, end=' ')
            print() # для відображення наступного рядка числа на новому рядку
        num += i

# Викличте функцію для друку шаблону із заданою кількістю рядків
print_alternate_pattern(5)

print('-----')

# exercise 21
# Напишіть програму для вирівнювання вкладеного списку за допомогою циклів
def flatten_list(nested_list):
    
    flat_list = []  # Ініціалізувати порожній список для зберігання зведених елементів

    # Перебираємо кожен елемент у списку
    for element in nested_list:
        if isinstance(element, list):  # Перевірте, чи є елемент списком
            for item in element:  # Якщо так, переберіть внутрішній список
                flat_list.append(item)
        else:
            flat_list.append(element)  # Якщо це не список, додайте елемент безпосередньо

    return flat_list

# Приклад використання
nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)

print('-----')

# exercise 22
# Напишіть програму на Python, яка визначає цифру з найбільшим 
# значенням і цифру з найменшим значенням у цьому числі.
num1 = 9876543210
num2 = -5082

def find_largest_smallest_digit(number):
 
  if number == 0:
    print("The number is zero. Largest and smallest digit is 0.")
    return 0, 0

  s_number = str(abs(number))  # Перетворити на рядок та обробити від'ємні числа
  largest_digit = int(s_number[0])
  smallest_digit = int(s_number[0])

  for digit in s_number[1:]:
    digit_int = int(digit)
    if digit_int > largest_digit:
      largest_digit = digit_int
    if digit_int < smallest_digit:
      smallest_digit = digit_int

  return largest_digit, smallest_digit

# приклади використання:

num1 = 9876543210
largest1, smallest1 = find_largest_smallest_digit(num1)
if largest1 is not None:
  print(f"Largest digit in {num1}: {largest1}")
  print(f"Smallest digit in {num1}: {smallest1}")

num2 = -5082
largest2, smallest2 = find_largest_smallest_digit(num2)
if largest2 is not None:
  print(f"Largest digit in {num2}: {largest2}")
  print(f"Smallest digit in {num2}: {smallest2}")