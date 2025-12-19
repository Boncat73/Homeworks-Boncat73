# exercise 1
# Напишіть програму на Python для створення класу Vehicle з 
# атрибутами екземпляра max_speed and mileage
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

print('-----')

# exercise 2
# Створення класу Vehicle без будь-яких змінних та методів
class Vehicle:
    pass

print('-----')

# exercise 3
# Створення дочірнього класу Bus, який успадковуватиме 
# всі змінні та методи класу Vehicle
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

Public_bus = Bus('Public Mersedes', 150, 15)
print('Vehicle name:', Public_bus.name, 'Speed:', Public_bus.max_speed, 'Mileage:', Public_bus.mileage)

print('-----')

# exercise 4
# Створіть клас Bus , який успадковується від класу Vehicle
# Надайте аргументу capacity значення за замовчуванням Bus.seating_capacity() 50 
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers.'

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
Public_bus = Bus('Public Mersedes', 150, 15)
print(Public_bus.seating_capacity())

print('-----')

# exercise 5
# Визначте атрибут класу « колір » зі значенням за замовчуванням 
# білий . Тобто, кожен транспортний засіб має бути білим
class Vehicle:
    # class atribute
    # color = 'White'
    def __init__(self, name, max_speed, mileage, color = 'White'):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Public_bus = Bus("School Mersedes", 150, 15)
print(Public_bus.color, Public_bus.name, "Speed:", Public_bus.max_speed, "Mileage:", Public_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

print('-----')

# exercise 6
# Успадкування класів
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(salf):
        return salf.capacity * 100
    
class Bus(Vehicle):
    def fare(salf):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
    
Public_bus = Bus('Public Mersedes', 12, 50)
print('Total Bus fare is: ', Public_bus.fare())

print('-----')

# exercise 7
# Напишіть програму, яка визначає, до якого класу належить заданий об'єкт Bus
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

Public_bus = Bus('Public Mersedes', 12, 50)
# Python`s built-in type()
print(type(Public_bus))

print('-----')

# exercise 8
# Визначення того, чи Public_bus також є екземпляром класу Vehicle
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

Public_bus = Bus('Public Mersedes', 15, 75)

# Python`s built-in insinstance() functions
print(isinstance(Public_bus, Vehicle))

print('-----')

# exercise 9
#  Перевірка, чи є об'єкт підкласом певного класу
class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print(issubclass(Dog, Animal)) # output True (Dog -> Animal)
print(issubclass(Animal, Dog)) # output False (Animal is not a subclass of Dog)
print(issubclass(Cat, Animal)) # output False (Cat is not related to Animal)
print(issubclass(Puppy, Animal)) # output True (Puppy inherits from Dog, which inherits from Animal)

print('-----')

# exercise 10
# Обчислення площі різних фігур за допомогою ООП
# Shape клас, підкласи Circle  та Square. Батьківський клас ( Shape) має area()метод
# ООП-код для обчислення площі кожної фігури (кожен підклас повинен мати 
# власну реалізацію area()методу для обчислення своєї площі)
import math

class Shape:
    def area(self):
        raise NotImplementedError('Area method must be implemented by subclasses')

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    # реалізуємо метод для кола
    def area(self):
        return math.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    # реалізуємо метод для квадрата
    def area(self):
        return self.side ** 2

# example of polymorthism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())

