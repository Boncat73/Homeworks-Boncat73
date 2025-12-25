# внутрішній клас - це клас,визначений в середині іншого класу
# він може отримати доступ до властивостей та методів зовнішнього класу
# внутрішні класи корисні для групування класів,які використовуються
# лише в одному місці,що робить код більш організованим
class Outer:
    def __init__(self):
        self.name = 'Outer Class'

    class Inner:
        def __init__(self):
            self.name = 'Inner Class'

        def display(self):
            print('This is the inner class.')

outer = Outer()
print(outer.name)

print('-----')

# щоб отримати доступ до внутрішнього класу треба створити обʼєкт 
# зовнішнього класу,а потім треба створити обʼєкт внутрішнього класу
class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display(self):
            print("Hello from inner class.")

outer = Outer()
inner = outer.Inner()
inner.display()

print('-----')

# внутрішні класи не мають автоматичного доступу до екземпляру 
# зовнішнього класу.Щоб отримати доступ,треба передати екземпляр 
# зовнішнього класу як параметр
class Outer:
    def __init__(self):
        self.name = 'Emil'

    class Inner:
        def __init__(self, outer):
            self.outer = outer

        def display(self):
            print(f'Outer class name: {self.outer.name}.')

outer = Outer()
inner = outer.Inner(outer)
inner.display()

print('-----')

# внутрішні класи корисні для створення допоміжніх класів,які використовуються
# лише в контексті зовнішнього класу
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # Створюємо екземпляр двигуна при створенні машини
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.status = 'Off'

        def start(self):
            self.status = 'Running'
            print('Engine started.')

        def stop(self):
            self.status = 'Off'
            print('Engine stopped.')

    def drive(self):
        # Звертаємося до конкретного об'єкта self.engine
        if self.engine.status == 'Running':
            print(f'Driving the {self.brand} {self.model}')
        else:
            print('Start the engine first!')

car = Car('Toyota', 'Corolla')
car.drive()        # Виведе: Start the engine first!
car.engine.start() # Виведе: Engine started.
car.drive()        # Виведе: Driving the Toyota Corolla

print('-----')

# Клас може мати кілька внутрішніх класів:
class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print('Processing data ...')

    class RAM:
        def store(self):
            print('Storing data ...')

computer = Computer()
computer.cpu.process()
computer.ram.store()

print('-----')

# exercise 1
# Комп'ютер та Процесор
# Створіть клас Computer з вкладеним класом Processor.
# Клас Processor повинен мати атрибут model і метод info(), 
# який виводить назву моделі.
# Клас Computer має створювати об'єкт Processor у своєму 
# конструкторі
class Computer:
    def __init__(self, brand, cpu_model):
        self.brand = brand
        self.processor = self.Processor(cpu_model)

    class Processor:
        def __init__(self, model):
            self.model = model

        def info(self):
            return f'Processor model: {self.model}.'
        
pc = Computer('Asus', 'Intel i7')
print(pc.processor.info())

print('-----')

# exercise 2
# Керування статусом (Світлофор)
# Створіть клас TrafficLight (Світлофор). Всередині нього 
# створіть клас Bulb (Лампочка).
# Лампочка повинна мати колір та стан (on чи off).
# Світлофор повинен мати три лампочки (червону, жовту, зелену).
# Додайте метод у TrafficLight, який вмикає лише одну 
# конкретну лампочку
class TrafficLight:
    def __init__(self):
        self.red = self.Buld('Red')
        self.yellow = self.Buld('Yellow')
        self.green = self.Buld('Green')

    class Buld:
        def __init__(self, color):
            self.color = color
            self.is_on = False

    def switch_to(self, color):
        for b in [self.red, self.yellow, self.green]:
            b.is_on = (b.color == color)
        print(f'Now {color} is ON.')

tl = TrafficLight()
tl.switch_to('Green')
print(f'Is red on? {tl.red.is_on}.')

print('-----')

# exercise 3
# Доступ до даних (Профіль користувача)
# Створіть клас User, який містить вкладений клас Profile.
# User зберігає username.
# Profile зберігає email та city.
# Реалізуйте метод у User, який виводить повну інформацію 
# про користувача, звертаючись до даних вкладеного класу
class User:
    def __init__(self, username, email, city):
        self.username = username
        self.Profile = self.Profile(email, city)

    class Profile:
        def __init__(self, email, city):
            self.email = email
            self.city = city

    def display_info(self):
        print(f'User: {self.username}')
        print(f'Contacts: {self.Profile.email}, Location: {self.Profile.city}')

user1 = User('Daniel', 'daniel@gmail.com', 'Kyiv')
user1.display_info()

print('-----')

# exercise 4
# Подвійне вкладення
# Створіть структуру з трьох рівнів: Клас World -> клас Country -> клас City.
# Кожен рівень повинен мати метод, що повертає назву.
# Продемонструйте створення об'єкта City через ланцюжок 
# звернень до класів
class World:
    class Country:
        def __init__(self, country_name):
            self.name = country_name

        class City:
            def __init__(self, city_name):
                self.name = city_name

# Створення об'єкта вкладеного класу "на льоту"
city = World.Country.City('Odessa')
print(f'City name: {city.name}.')

print('-----')

# exercise 5
# Валідатор (Логіка у вкладеному класі)
# Створіть клас SmartPhone. У ньому — вкладений клас Battery.
# Battery має рівень заряду (0-100).
# У Battery має бути метод charge(amount), який не дозволяє 
# заряду перевищити 100.
# У SmartPhone має бути метод status(), який повідомляє, 
# чи потрібна підзарядка (якщо заряд < 20%)
class SmartPhone:
    def __init__(self):
        self.battery = self.Battery()

    class Battery:
        def __init__(self):
            self.level = 10

        def charge(self, amount):
            self.level = min(100, self.level + amount)
            print(f"Charging... Level: {self.level}%")

    def status(self):
        if self.battery.level < 20:
            return "Battery low! Please charge."
        return "Battery OK."

phone = SmartPhone()
print(phone.status())
phone.battery.charge(50)
print(phone.status())