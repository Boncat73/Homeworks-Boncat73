# успадкування

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

p1 = Person('Daniel', 'Bondarevskyi')
p1.printname()

print('-----')

class Student:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Student('Mike', 'Olsen')
x.printname()

print('-----')

# без функції super()
class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.
        Person.__init__(self, fname, lname) # !!!

# функція super()змушує дочірній клас успадкувати усі 
# методи та властивості від свого батьківського класу
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) # !!!

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year # add properties
    
x = Student('George', 'Bondarevskyi', 2019)
print(x.graduationyear)

print('-----')

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print(f'Welcome, {self.fname}, {self.lname}, to the class of.')

x = Student('Vasy', 'Bondarevskyi', 2019)
x.welcome()

# базове успадкування
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

class Car(Vehicle):
    def __init__(self, make, year, fuel_type):
        super().__init__(make, year) # викликаємо конструктор батька
        self.fuel_type = fuel_type

my_car = Car('Toyota', 2021, 'Gasoline')
print(f'{my_car.make},{my_car.year},{my_car.fuel_type}')

print('-----')

# перевизначення методів
class Animal:
    def speak(self):
        return 'Animal has a voice.'
        
class Dog(Animal):
    def speak(self):
        return 'Gav!'
    
class Cat(Animal):
    def speak(self):
        return 'Meao!'
    
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

print('-----')

# робота super() у методах
class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name
    
class Managar(Employee):
    def get_details(self):
        parent_details = super().get_details()
        return f'{parent_details} (Manager)'
    
m = Managar('Vasyl')
print(m.get_details())
    
print('-----')

# ієрархія класів (багаторівневе успадкування)
class Device:
    def __init__(self, brand):
        self.brand = brand

class Computer(Device):
    def __init__(self, brand, processor):
        super().__init__(brand)
        self.processor = processor

class Laptop(Computer):
    def __init__(self, brand, processor, battery_life):
        super().__init__(brand, processor)
        self.battery_life = battery_life

my_laptop = Laptop('Apple MacBook PRO', 'Intel I7', '18 hourse')
print(f'Brand: {my_laptop.brand}, CPU: {my_laptop.processor}, Battery: {my_laptop.battery_life}')

print('-----')

# множинне успадкування
class Flyable:
    def fly(self):
        return 'I am flying!'
    
class Swimmable:
    def swim(self):
        return 'I am swimming!'
    
class Duck(Flyable, Swimmable):
    pass

donald = Duck()
print(donald.fly())
print(donald.swim())
print(donald.fly(), donald.swim())
print(f'Ok, I am duck, because {donald.fly()} And {donald.swim()}!!!')

