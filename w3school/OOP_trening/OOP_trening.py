class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print('Hello, my name is ', self.name)

p2 = Person('Daniel', 23)

del p2

#print(p2) # here is maistake because we remove del p2

print('-----')

class Myclass:
    x = 5

p3 = Myclass()
p4 = Myclass()
p5 = Myclass()

print(p3.x)
print(p4.x)
print(p5.x)

class Person:
    pass

print('-----')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name} and I have {self.age} years old.'
    
pers1 = Person('Adaline', 25)
print(pers1.name)
print(pers1.age)
print(pers1)

print('-----')

class Person:
    pass

p6 = Person()
p6.name = 'Michle'
p6.age = 42
print(p6.name)
print(p6.age)

print('-----')

class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name} amf I have {self.age}'
    
p7 = Person('Vasyl', 52)
p8 = Person('Anne')
print(p7.name, p7.age)
print(p8.name, p8.age)

print('-----')

class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def __str__(self):
        return f'I am {self.name}, I have {self.age} years old, I am from {self.city} in the {self.country}'
    
person1 = Person('Vasyl', 52, 'Nikopol', 'Ukraine')
person2 = Person('Daniel', 23, 'Nikopol', 'Ukraine')
person3 = Person('George', 21, 'Nikopol', 'Ukraine')

print(person1.name, person1.age, person1.city, person1.country)
print(person2.name, person2.age, person2.city, person2.country)
print(person3.name, person3.age, person3.city, person3.country)

print('-----')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, my name is {self.name}, I have {self.age} years old.')

    def say(self):
        return f'I want to say: Python is great!!!)'
    
person4 = Person('Vasyl', 52)
person4.greet()
print(person4.say())

print('-----')

class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)

person5 = Person('Vasyl')
person6 = Person('Tobias')

person5.printname()
person6.printname()

print('-----')

class Person:
    def __init__(my_fantasy, name, age):
        my_fantasy.name = name
        my_fantasy.age = age

    def say(abc):
        print('Hello, my name is ' + abc.name)

person7 = Person('Vasyl', 52)
person7.say()

print('-----')

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(f'{self.brand} {self.model} {self.year}')

car1 = Car('Volvo', 'S350', '2024')
car1.display()

print('-----')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Hello, {self.name}!'
    
    def welcome(self):
        message = self.greet()
        print(f'{message}! Welcome to us!')

person8 = Person('John', 28)
person8.welcome()

print('-----')

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car2 = Car('Mersedes', 'S-Class')
print(car2.brand, car2.model)

car2.model = 'L-Class'
print(car2.model)

del car2.model

print(car2.brand) # this works
#print(car2.model) # this would cause an error!

print('-----')

class Person:
    species = 'Human' # Class property

    def __init__(self, name):
        self.name = name

pers2 = Person('George')
pers3 = Person('Daniel')

print(pers2.name)
print(pers3.name)
print(pers2.species)
print(pers3.species)

print('-----')

class Person:
    lastname = ''

    def __init__(self, name):
        self.name = name

pers4 = Person('Vasyl')
pers5 = Person('Daniel')
pers6 = Person('George')

Person.lastname = 'Bondarevskyi'

print(pers4.lastname)
print(pers5.lastname)
print(pers6.lastname)

print(pers4.name, pers4.lastname)
print(pers5.name, pers5.lastname)
print(pers6.name, pers6.lastname)

print('-----')

class Person:
    def __init__(self, name):
        self.name = name

pers7 = Person('Vasyl')

pers7.age = 52
pers7.city = 'Nikopol'
pers7.country = 'Ukraine'

print(f'{pers7.name} {pers7.age} {pers7.city} {pers7.country}')

print('-----')

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, my name is ' + self.name)

p9 = Person('Emil')
p9.greet()

print('-----')

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

print('-----')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'{self.name} is {self.age} years old.')

p10 = Person('Emil', 27)
print(p10.get_info())

print('-----')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f'Happy birthday! You are now {self.age}')

p11 = Person('Vasyl', 52)
p11.celebrate_birthday()
p11.celebrate_birthday()

print('-----')

# without __str__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p12 = Person('Emil', 34)
print(p12)

# with __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'

p1 = Person("Tobias", 36)
print(p1)

print('-----')

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_songs(self, song):
        self.songs.append(song)
        print(f'Added: {song}')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Removed: {song}')

    def show_songs(self):
        print(f'Playlist "{self.name}":')
        for song in self.songs:
            print(f'- {song}')

my_playlist = Playlist('Favorites')
my_playlist.add_songs('Bohemian Rhapsody')
my_playlist.add_songs('Stairway to Heaven')
my_playlist.show_songs()

print('-----')

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello!')

p13 = Person('Emil')

del Person.greet

#p13.greet() # this will cause an error

