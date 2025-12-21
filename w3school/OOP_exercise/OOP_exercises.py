# exercise 1
# Основи створення класу
# Створіть клас Book, який має атрибути title (назва) 
# та author (автор). Реалізуйте метод description(), 
# який виводить рядок у форматі: "Книга 'Назва', автор: Автор"
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f'Book: {self.title}, author: {self.author}.'
    
my_book = Book('Кобзар', 'Тарас Григорович Шевченко')
print(my_book.description())

print('-----')

# exercise 2
# Методи та розрахунки
# Створіть клас Rectangle (прямокутник). Він повинен приймати width (ширину) 
# та height (висоту). Додайте методи area() для обчислення площі та 
# perimeter() для периметра
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
rect = Rectangle(10, 4)
print(f"Area is: {rect.area()}, Perimeter is: {rect.perimeter()}.")

print('-----')

# exercise 3
# Інкапсуляція (Приватні атрибути)
# Створіть клас BankAccount. Зробіть атрибут __balance приватним. 
# Реалізуйте методи deposit(amount) (поповнення) та get_balance() 
# (перегляд залишку). Перевірте, щоб не можна було змінити баланс напряму
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Приватний атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сума має бути додатною")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # Це викличе помилку AttributeError

print('-----')

# exercise 4
# Успадкування
# Створіть базовий клас Vehicle (Транспорт) з атрибутами brand і year. 
# Створіть дочірній клас Car, який додає атрибут fuel_type. 
# Викличте метод батьківського класу через super()
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, fuel_type):
        super().__init__(brand, year)
        self.fuel_type = fuel_type

    def info(self):
        return f'{self.brand} ({self.year}), gasoline: {self.fuel_type}'
    
tesla = Car('Tesla', 2023, 'Electric')
print(tesla.info())

print('-----')

# exercise 5
# Поліморфізм (Перевизначення методів)
# Створіть два класи Dog та Cat. У обох має бути метод speak(). 
# Собака каже "Гав!", кіт — "Мяу!". Напишіть функцію 
# animal_sound(animal), яка приймає об'єкт і викликає його 
# метод speak()
class Dog:
    def speak(self):
        return 'Gav!'
    
class Cat:
    def speak(self):
        return 'Mao!'
    
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

print('-----')

# exercise 6
# Атрибути класу vs Атрибути об'єкта
# Створіть клас Student, який має атрибут класу 
# school_name = "IT Step". Кожен об'єкт повинен мати ім'я name. 
# Створіть 2 студентів та змініть назву школи для всіх одразу.
class Student:
    school_name = 'Academy for heroes' # атрибут класу

    def __init__(self, name):
        self.name = name # атрибут класу

s1 = Student('Daniel')
s2 = Student('George')

print(s1.school_name) # Academy for heroes
Student.school_name = 'Universaty' # зміна для всіх
print(s2.school_name) # Universaty

print('-----')

# exercise 7
# Методи класу (@classmethod)
# Реалізуйте клас Employee, який рахує загальну кількість створених 
# працівників за допомогою атрибута класу count та методу 
# класу get_count()
class Employee:
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def get_count(cls):
        return f'Всього праівників: {cls.count}'
    
e1 = Employee('Daniel')
e2 = Employee('George')
print(Employee.get_count())

print('-----')

# exercise 8
# Декоратор @property (Гетери та сетери)
# Створіть клас Celsius. Використовуйте @property для атрибута 
# temperature. Додайте сетер, який не дозволяє встановлювати 
# температуру нижче -273.15°C
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature
    
    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            print('Температура не може бути нижче абсолютного нуля!')
        else:
            self._temperature = value

temp = Celsius(20)
temp.temperature = -300 # виведе попередження
print(temp._temperature) # 20

print('-----')

# exercise 9
# Магічні методи (__str__ та __add__)
# Створіть клас Vector, який приймає координати x та y. 
# Реалізуйте __str__ для гарного виводу та __add__, щоб можна було 
# додавати два вектори за допомогою оператора +
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 4)
v2 = Vector(5, -2)

print(v1 + v2) # Vector(7, 2)

print('-----')

# exercise 10
# Абстрактні класи
# Використовуючи модуль abc, створіть абстрактний клас Shape з 
# методом area(). Створіть клас Circle, який успадковує Shape 
# та реалізує цей метод
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    
c = Circle(5)
print(f'Площа кола: {round(c.area(), 2)}')

print('-----')

# exercise 11
# перший варіант рішення з імпортом модулю datetime
from datetime import datetime

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def greeting(self):
        print(f"Привіт! Я {self.name} {self.surname}.")

class Student(Person):
    def __init__(self, name, surname, course_year):
        # Викликаємо конструктор батьківського класу 
        super().__init__(name, surname)
        self.course_year = course_year

    def greeting(self, middle_name):
        # Перевизначена функція, що приймає по батькові
        print(f"Вітаю! Я {self.surname} {self.name} {middle_name}.")

    def get_course(self):
        current_year = datetime.now().year
        course = current_year - self.course_year + 1
        
        if course <= 0:
            return "Навчання ще не розпочалося"
        elif course > 6:
            return "Навчання вже завершено (або це аспірантура)"
        else:
            return f"{course}-й курс"

# Створюємо об'єкт класу Person
person1 = Person("Олексій", "Петренко")
person1.greeting()

print("---")

# Створюємо об'єкт класу Student
student1 = Student("Василь", "Бондаревський", 2025)
# Викликаємо привітання з по батькові
student1.greeting("Юрійович")
# Рахуємо курс
print(f"Рік навчання: {student1.get_course()}")

print('-----')

# другий варіант рішення без модулю datetime
# from datetime import datetime

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def greeting(self):
        print(f"Привіт! Я {self.name} {self.surname}.")

class Student(Person):
    def __init__(self, name, surname, course_year):
        # Викликаємо конструктор батьківського класу
        super().__init__(name, surname)
        self.course_year = course_year

    def greeting(self, middle_name):
        # Перевизначена функція, що приймає по батькові
        print(f"Вітаю! Я {self.surname} {self.name} {middle_name}.")

    def get_course(self):
        current_year = datetime.now().year
        course = current_year - self.course_year + 1
        
        if course <= 0:
            return "Навчання ще не розпочалося"
        elif course > 6:
            return "Навчання вже завершено (або це аспірантура)"
        else:
            return f"{course}-й курс"

# Створюємо об'єкт класу Person
person1 = Person("Олексій", "Іванов")
person1.greeting()

print("---")

# Створюємо об'єкт класу Student
student1 = Student("Василь", "Бондаревський", 2025)
# Викликаємо привітання з по батькові
student1.greeting("Юрійович")
# Рахуємо курс
print(f"Рік навчання: {student1.get_course()}")

print('-----')

# другий варіант рішення
class Person1:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def greeting(self):
        print(f'{self.name} {self.surname}')

class Student1(Person1):
    def __init__(self, name, surname, year):
        super().__init__(name, surname)
        self.year = year

    def greeting(self, middlename):
        print(f'{self.name} {self.surname} {middlename}.')

    def year0Study(self):
        currentYear =  2025
        print(f'Year of study of student: {currentYear - self.year + 1}')

per1 = Person('Ivan', 'Ivanenko')
st1 = Student1('Petro', 'Petrenko', 2025)

st1.greeting('Petrovich')
st1.year0Study()