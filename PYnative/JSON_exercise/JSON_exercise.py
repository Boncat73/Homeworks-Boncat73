# exercise 1
# Перетворіть наступний словник у формат JSON
import json

data = {
    'key1': 'value1',
    'key2': 'value2'
}

jsonData = json.dumps(data)

print('-----')

# exercise 2
# Отримайте доступ до значення key2 з наступного JSON
import json

# Зверніть увагу на лапки навколо всього об'єкта
sampleJson_string = '{"key3": "value3", "key4": "value4"}'

data = json.loads(sampleJson_string) # Тепер це спрацює
print(data['key4'])

print('-----')

# exercise 3
# 
import json

sampleJson = {"key1" : "value2", "key2" : "value2", "key3" : "value3"}
prettyPrintedJson  = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

print('-----')

# exercise 4
# Сортування ключів JSON та запис їх у файл
import json

sampleJson = {'id': 1, 'name': 'value2', 'age': 29}

print('Started writing JSON data into a file.')
with open('sampleJson', 'w') as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)

print('Done writing JSON data into a file.')

print('-----')

# exercise 5
# Отримайте доступ до вкладеного ключа «зарплата» 
# з наступного JSON
import json

sampleJson = """{
    "company": {
        "employee":{
            "name": "Emma",
            "payble":{
                "salary": 7000,
                "bonus": 800
            }
        }
    }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payble']['salary'])

print('-----')

# exercise 6
# Перетворіть наступний об'єкт Vehicle у формат JSON
import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert it into JSON format
print("Encode Vehicle Object into JSON.")
vehicleJson = json.dumps(vehicle, indent=4, cls=VehicleEncoder)
print(vehicleJson)

print('-----')

# exercise 7
# Перетворіть наступний JSON на об'єкт Vehicle
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

def vehicleDecoder(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

vehicleObj = json.loads('{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}', object_hook=vehicleDecoder)

print(f'Type of decoded object from JSON Data {type(vehicleObj)}')
print(f'Vehicle Details: {vehicleObj.name, vehicleObj.engine, vehicleObj.price}')

print('-----')

# exercise 8
# Перевірте, чи є наступний json коректним чи 
# некоректним. Якщо некоректний, виправте його
# рішення 1: 
# виконуємо у терміналі команду: echo "JSON DATA" | python -m json.tool
import json

# 1. Додаємо кому між "зарплата" та "бонус"
# 2. Присвоюємо словник змінній (наприклад, data)
data = {
   "компанія": {
      "співробітник": {
         "ім'я": "емма",
         "до сплати": {
            "зарплата": 7000,  # Тут була пропущена кома
            "бонус": 800
         }
      }
   }
}

# Тепер ми можемо дістати значення, наприклад, бонус:
print(f"Бонус: {data['компанія']['співробітник']['до сплати']['бонус']}")

# рішення 2: просто додаємо кому
import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print(f'Given JSON string is Valid: {isValid}')

print('-----')

# exercise 9
# Розберіть наступний JSON, щоб отримати 
# всі значення ключа 'name' в масиві
import json

# JSON-рядок, який імітує дані, отримані, наприклад, через API
# Зверніть увагу, що це текст (рядок), про що свідчать потрійні лапки
sampleJson = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []

try:
    # Перетворюємо JSON-рядок у формат Python 
    # (у даному випадку — у список словників)
    data = json.loads(sampleJson)
except Exception as e:
    # Якщо в JSON буде помилка (наприклад, зайва 
    # кома або відсутня дужка), виведемо її
    print(f"Помилка при читанні JSON: {e}")

# Використовуємо List Comprehension (генератор списків), 
# щоб дістати лише імена
# Метод .get('name') безпечніший, ніж звернення 
# через ['name'], 
# бо не видасть помилку, якщо ключа "name" раптом не 
# буде в об'єкті
dataList = [item.get('name') for item in data]

# Виводимо отриманий список імен: ['name1', 'name2']
print(dataList)
