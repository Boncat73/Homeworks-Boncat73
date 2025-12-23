# поліморфізм

x = 'Hello World!'
print(len(x))

print('-----')

myTuple = ('apple', 'banana', 'apricot', 'mango')
print(len(myTuple))

print('-----')

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

print(len(thisdict))

print('-----')

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('I can drive!')

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('I can sail!')

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('I can fly!')

car1 = Car('Mersedes', 'SL500') # create a Car object
boat1 = Boat('Ibiza', 'Touring 20') # create a Boat jbject
plane1 = Plane('Boeing', '747') # create a Plane object

for x in (car1, boat1, plane1):
    x.move()

print('-----')

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print('I can move!')

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('I can sail!')
    
class Plane(Vehicle):
    def move(self):
        print('I can fly!')

car2 = Car('Ford', 'Mustang')
boat2 = Boat('Ibiza', 'Touring 20')
plane2 = Plane('Boeing', '747')

for x in {car2, boat2, plane2}:
    print(x.brand)
    print(x.model)
    x.move()

print('-----')

# поліморфізм у методах класів
# Створіть два класи Square (Квадрат) та Circle (Коло). 
# Кожен клас повинен мати метод area(). Створіть список 
# з об'єктів обох типів і в циклі виведіть площу кожного
import math
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * 2
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
shapes = [Square(5), Circle(3), Square(2)]

for shape in shapes:
    print(f'Area the figure is: {shape.area():.2f}')

print('-----')

# поліморфізм через спільну функцію
# Створіть класи Piano та Guitar. Обидва мають метод play(). 
# Напишіть функцію start_concert(instrument), яка викликає 
# метод play() незалежно від того, який інструмент їй передали
class Piano:
    def play(self):
        return 'Грають клавіші піаніно.'
    
class Guitar:
    def play(self):
        return 'Бринять струни гітари.'
    
def start_concert(instrument):
    print(instrument.play())

piano = Piano()
guitar = Guitar()

start_concert(piano)
start_concert(guitar)

print('-----')

# качина типізація (Duck Typing)
# Створіть клас Bird з методом fly() та клас Airplane, який 
# також має метод fly(). Продемонструйте, що Python дозволяє 
# викликати fly() для обох об'єктів в одній функції, хоча 
# вони не мають спільного батьківського класу
class Bird:
    def fly(self):
        print('Птах махає крилами.')

class Airplane:
    def fly(self):
        print('Літак запускає двигуни і злітає.')

def lift_off(entity):
    entity.fly()

object = [Bird(), Airplane()]

for obj in object:
    lift_off(obj)

print('-----')

# абстрактні базові класи (АВС)
# Використовуючи модуль abc, створіть абстрактний клас Payment 
# з методом process(). Створіть дочірні класи CreditCard та PayPal, 
# які реалізують цей метод по-різному
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self):
        pass

class CreditCard(Payment):
    def process(self):
        return 'Обробка транзакції через банківську карту.'
    
class PayPal(Payment):
    def process(self):
        return 'Авторизація та переказ через PayPal.'
    
payments = [CreditCard(), PayPal()]
for p in payments:
    print(p.process())

print('-----')

# поліморфізм вбудованих функцій
# Продемонструйте поліморфізм на прикладі вбудованої функції len(). 
# Покажіть, як вона працює з рядком, списком та словником. 
# Поясніть, чому це є прикладом поліморфізму
string = 'Python'
my_list = [10, 20, 30]
my_dict = {'a': 1, 'b': 2}

print(len(string)) # повертає кількість символів
print(len(my_list)) # повертає кількість елементів
print(len(my_dict)) # повертає кількість ключів

# Пояснення: len() є поліморфною функцією, оскільки вона вміє 
# працювати з обʼєктами різних класів, викликаючи 
# внутрішній магічний метод __len__() цих обʼєктів.