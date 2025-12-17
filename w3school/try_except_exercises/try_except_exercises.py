# exercise 1
# функція,яка приймає два числа та повертає результат їхнього ділення,вико-
# ристовується try...except для обробки винятку ZeroDivisionError,
# якщо друге число дорівнює нулю
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return 'Помилка, ділення на нуль неможливе.'
    except TypeError:
        return 'Помилка, обидва аргументи мають бути числами.'
    else:
        return f'Результат ділення: {result}.'
    
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, 'a'))

print('-----')

# exercise 2
# обробка невірного типу даних при введенні
def get_valid_integer():
    while True:
        try:
            user_input = input('Введіть ціле число: ')
            number = int(user_input)
        except ValueError:
            print('Невірний ввід.Будь ласка,введіть саме ціле число.')
            continue # повторюємо цикл
        else:
            print(f'Ви ввели число: {number}.')
            break # виходимо з циклу,якщо він успішний

get_valid_integer()

print('-----')

# exercise 3
# обробка винятків при роботі зі словником (KeyError)
def get_dict_value(dictionary, key):
    # повертає значення словника або повідомлення про помилку,якщо ключ не знайдено
    try:
        value = dictionary[key]
    except KeyError:
        return f'Помилка: ключ {key} не знайдено у словнику.'
    else:
        return f"Значення для ключа '{key}': {value}."
    
data = {'name': 'Alice', 'age': 30}
print(get_dict_value(data, 'name'))
print(get_dict_value(data, 'city'))

print('-----')

# exercis 4
# обробка винятків при роботі зі списками (IndexError)
def get_list_element(input_list, index):
    # повертає елемент списку за індексом або повідомлення про помилку
    try:
        element = input_list[index]
    except IndexError:
        return f'Помилка: індекс {index} знаходиться поза межами списку (розмір: {len(input_list)}.)'
    else:
        return f'Елемент за індексом {index}: {element}.'
    
my_list = [10, 20, 30]
print(get_list_element(my_list, 1))
print(get_dict_value(my_list, 2)) # error after index equal 3

print('-----')

# exercise 5
# Імітуйте функцію, яка відкриває файл. Використовуйте конструкцію 
# try...finally, щоб гарантувати, що повідомлення "Закриття ресурсу" 
# завжди буде виведене на екран, незалежно від того, чи стався 
# виняток у блоці try.
def process_file_resourse(should_fail):
    # імітує роботу з файлом,використовуючи finally
    try:
        print('Відкриття файлового ресурсу ...')
        if should_fail:
            # спровокуємо помилку для тестування блоку finally
            result = 10 / 0
        else:
            print('Обробка файлу успішна.')
    except ZeroDivisionError:
        print('Виняток: ділення на нуль!')
        return 'Обробка завершена з помилкою.'
    finally:
        # цей блок завжди виконується
        print('Закриття ресурс. finally завжди спрацьовує!')
    return 'Обробка завершена успішно.'

print('\n---Сценарій 1: успішне виконання---')
process_file_resourse(False)
print('\n---Сценарій 2: Виняток---')
process_file_resourse(True)

print('-----')

# exercise 6
# Напишіть функцію, яка приймає список і індекс. Спробуйте отримати 
# елемент за індексом і перетворити його на число. Використовуйте 
# кілька except блоків для обробки IndexError (якщо індекс недійсний) 
# та ValueError (якщо елемент не може бути перетворений на число)
def safe_convert_to_number(data_list, index):
    # отримує елемент за індексом і конвертує його в число,обробляючи помилки
    try:
        # отримання елементу
        element = data_list[index]
        print(f'Отриманий елемент: {element}')
        # конвертація
        number = float(element)
    except IndexError:
        print(f'Помилка: індекс {index} поза межами списку.')
    except ValueError:
        print(f"Помилка: елемент '{element}' не може бути перетворений на число.")
    except Exception as e:
        # обробка будь-якого іншого непередбачуваного винятку
        print(f'Сталася непередбачувана помилка: {e}.')
    else:
        return f'Успішна конвертація: {number}.'
    
mixed_list = [10, '2.5', 'hello', 4]
print(mixed_list)
print(safe_convert_to_number(mixed_list, 0))
print(safe_convert_to_number(mixed_list, 2))
print(safe_convert_to_number(mixed_list, 10))

print('-----')

# exercise 7
# обробка винятків при роботі з файлами (FileNotFoundError)
# Напишіть функцію, яка намагається прочитати вміст файлу з 
# заданим ім'ям. Обробіть виняток FileNotFoundError, якщо файл не існує
def read_file_safely(filename):
    # читає файл,обробляючи відсутність файлу
    content = ""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return None
    except Exception as e:
        print(f"Виникла інша помилка при роботі з файлом {e}.")
        return None
    else:
        print(f"Файл '{filename}' успішно прочитано.")
        return content
    
# файл 'non_existent_file.txt' має не існувати для тесту
file_content = read_file_safely("non_existent_file.txt")
# print(file_content) # буде None

print('-----')

# exercise 8
# Напишіть функцію, яка приймає вік користувача. Якщо вік менше 0 
# або більше 120, вона повинна викликати (підняти) 
# виняток ValueError з відповідним повідомленням
def validate_age(age):
    # перевіряє вік і піднімає ValueError, якщо він недійсний
    if not isinstance(age, int):
        raise TypeError('Вік має бути цілим числом.')
    
    if age < 0 or age > 120:
        raise ValueError('Недійсний вік. Вік має бути від 0 до 120.')
    else:
        return f'Вік {age} є дійсним.'
    
# приклади використання з try...except
try:
    print(validate_age(30))
    print(validate_age(150))
except ValueError as e:
    print(f'Обробка винятку: {e}.')
except TypeError as e:
    print(f'Обробка винятку: {e}.')

print('-----')

# exercise 9
# Напишіть функцію, яка намагається виконати операцію, 
# яка може призвести до KeyError або AttributeError. 
# Обробте обидва ці винятки в одному блоці except
class MyObject:
    pass

def complex_operation(data, key):
    # виконує операцію,що може викликати KeyError або AttributeError
    try:
        if isinstance(data, dict):
            # може викликати KeyError
            value = data[key]
        elif isinstance(data, MyObject):
            # може викликати AttributeError
            value = data.non_existent_attribute
        else:
            value = data[key] # припускаємо,що це інший тип

    except (KeyError, AttributeError):
        # обробка обох типів винятків одночасно
        print('Помилка: невірний ключ у словнику або відстутній атрибут обʼєкта.')
        return None
    except TypeError as e:
        print(f'Помилка: невірний тип даних для індексації/доступу: {e}.')
        return None
    else:
        return f'Операція успішна.Значення: {value}.'
    
# приклади
print(complex_operation({'a': 1}, 'b')) # KeyError
print(complex_operation(MyObject(), 'a')) # AttributeError
print(complex_operation({'a', 1}, 'a')) # Успіх

print('-----')

# exercise 10
# Напишіть функцію, яка імітує критичну операцію 
# (наприклад, ділення на нуль). Замість простого виведення 
# на екран, запишіть деталі винятку, включаючи його тип і 
# повідомлення, у спеціальний блок (наприклад, використовуючи 
# logging або простий print для імітації)
import sys
import traceback

def critical_calculation(numerator, denominator):
    # виконує ділення і логує виняток у разі помилки
    try:
        result = numerator/denominator
        return f'Result is: {result}'
    except Exception as e:
        # логування детальної інформації про виняток
        error_type = type(e).__name__
        error_message = str(e)

        # імітація логування (у реальному проектіі тут був би модуль logging)
        print('\n---КРИТИЧНЕ ЛОГУВАННЯ ПОМИЛКИ---')
        print(f'Тип винятку: {error_type}')
        print(f'Повідомлення: {error_message}')
        print('Деталі трасування:')
        # виведення повного трасування стека
        traceback.print_exc(file=sys.stdout)
        print('---------------------------------\n')
        return 'Помилка обчислення.Дивіться логи для деталей.'
    
# приклади
print(critical_calculation(10, 2))
print(critical_calculation(10, 0))
