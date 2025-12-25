# створення приватних властивостей через подвійне підкреслення
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # private property

p1 = Person('Emil', 25)
print(p1.name)
#print(p1.__age) # this will cause an error

print('-----')

# метод отримання доступу до приватної властивості getter() 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
p1 = Person('Tobias', 26)
print(p1.get_age())

print('-----')

# змінення приватної властивості через створення методу setter()
# setter() також може перевірити значення перед його встановленням
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Age must be positiv!')

p1 = Person('Tobias', 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

print('-----')

# інкапсуляція надає наступні переваги:
# захист даних: запобігає випадковій зміні даних
# перевірка: можна перевірити дані перед їх налаштуванням
# гнучкість: внутрішня реалізація може змінюватися без впливу на зовнішній код
# контроль: ви маєте повний контроль над тим, як здійснюється доступ до даних та як вони змінюються

# захист та перевірка даних
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print('Grade must be between 0 and 100.')

    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return 'Passed'
        else:
            return 'Failed'
        
student = Student('Emil')
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

print('-----')

# _ - protected існує, але захищення не працює по домовленності
# призначена для внутрішнього використання
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # protected property

p1 = Person('Linus', 50000)
print(p1.name)
print(p1._salary) # can access, but shouldn`t

print('-----')

# методи також можна робити приватними за допомогою __
class Calculator:
    def __init__(self):
        self.result = 0

    def __validate(self, number):
        if not isinstance(number, float):
            return False
        return True
    
    def add(self, number):
        if self.__validate(number):
            self.result += number
        else:
            print('Invalid number.')

calc = Calculator()
calc.add(10.0)
calc.add(5.0)
print(calc.result)
#calc.__validate(5) # this would cause an error

print('-----')

# name Mangling
# коли використовується подвійне підкреслення, Python автоматично 
# перейминовує його внутрішньо,додаючи попереду _ClassName,наприклад,
# __age стає _Person__age.
# спотворення імен - це те,як Python реалізує приватні властивості та методи.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

p1 = Person('Emil', 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!Це суперечить меті інкапсуляції!

print('-----')

# exercise 1
# створіть клас з атрібутами різного рівня доступу та надрукуйте 
# ці атрібути

class Smartphone:
    def __init__(self, brand, model, imei):
        self.brand = brand  # public 
        self._model = model # protected
        self.__imei = imei  # private

phone_1 = Smartphone('Apple', 'Iphone 15', '43958347658385' )

print(phone_1.brand)  # працює Apple
print(phone_1._model) # працює Iphone 15
# print(phone_1.__imei) # працює 43958347658385 тут буде помилка!!!

print('-----')

# exercise 2
# геттери та сеттери
# створіть клас,де баланс є приватним; створіть методи для перегляду
# та поповнення рахунку; додайте перевірку: не можна поповнювати 
# рахунок на відʼємну суму
class BankAccount:
    def __init__(self, initial_balance):
        self.initial_balance = initial_balance

    def get_balance(self):
        return f'Ваш баланс : {self.__balance} грн.'
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print (f'Ваш рахунок поповнено на {amount} грн.')
        else:
            print (f'Сума має бути додатною.')

print('-----')

# exercise 3
# Використання декоратора @property
# Створіть клас Employee. Зробіть атрибут __salary приватним. 
# Використовуйте декоратор @property, щоб створити геттер для зарплати, 
# та @salary.setter, щоб можна було змінювати зарплату, але лише 
# якщо нове значення більше за 0
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print('Зарплатня не може бути меншою за 0!')

emp = Employee('Petro', 20000)
emp.salary = 25000 # працює як звичайний атрибут завдяки @property
print(f'Salary is: {emp.name}: {emp.salary}')

print('-----')

# exercise 4
# Інкапсуляція логіки (Валідація даних)
# Створіть клас User, який приймає пароль. Пароль має бути приватним. 
# Напишіть метод для зміни пароля set_password, який вимагає спочатку 
# ввести старий пароль для перевірки
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password == new_password
            print('Пароль успішно змінено.')
        else:
            print('Старий пароль не вірний! Доступ заборонено!')

user1 = User('admi', '1234')
user1.set_password('1234', 'qwerty')  # успішно
user1.set_password('wrong', 'hacker') # помилка

print('-----')

# exercise 5
# Обчислювальні властивості (Read-only)
# Створіть клас Rectangle з приватними атрибутами __width та __height. 
# Реалізуйте доступ до них через @property. Також створіть властивість 
# area (площа), яку можна лише читати (без сеттера), оскільки вона 
# обчислюється автоматично
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def area(self):
        # це властивість read-only
        return self.__width * self.__height
    
rect = Rectangle(10,4)
print(f'Width: {rect.width}')
print(f'Height: {rect.height}')
print(f'Area: {rect.area}')
print(f'Area is : {rect.width} * {rect.height} = {rect.area}.')
# rect.area = 100 # AttributeError: property 'area' of 'Rectangle' object has no setter
