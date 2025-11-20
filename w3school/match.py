# обробка станів світлофора
def handle_traffic_light(state):
    match state:
        case "green":
            return "Можна їхати."
        case "yellow":
            return "Увага, приготуватися до зміни сигналу."
        case "red":
            return "Зупинитися, чекати."
        case _:
            return "Невідомий стан світлофора."
        
# test
print(f"Green: {handle_traffic_light("green")}.")
print(f"Yellow: {handle_traffic_light("yellow")}.")
print(f"Red: {handle_traffic_light("red")}.")
print(f"Blue: {handle_traffic_light("blue")}.")

print("-" * 30)

# аналіз даних користувача (зіставлення кортежів та змінних)
# Тут ми зіставляємо структуру кортежу і видобуваємо значення 
# у змінні (name, age). Зверніть увагу, що найбільш специфічний 
# шаблон (("Kyiv")) стоїть першим.

def analyze_user_data(data):
    match data:
        case (name, age, "Kyiv"):
            return f"User {name} from Kyiv."
        case (name, age):
            return f"User {name}, age {age}."
        case _:
            return "Isn`t correct data."
        
# test
print(f"Data 1: {analyze_user_data(("Oleg", 35, "Kyiv"))}")
print(f"Data 2: {analyze_user_data(("Anna", 28))}")
print(f"Data 3: {analyze_user_data(("Dmitro", 40, "Lviv"))}")
print(f"Data 4: {analyze_user_data(("Taras",))}")

print("-" * 30)

# Обробка команд гри (Зіставлення зі списками та Умовами if)
# Ця задача демонструє використання умов if всередині блоку 
# case (так звані Guard-умови) та зіставлення зі списками.

def process_game_command(command):
    match command:
        # 1. Команда 'move' з діагональним рухом (використовуємо 'if' умову)
        case ["move", x, y] if x == y:
            return f"Діагональний рух: ({x}, {y})"
        # 2. Команда 'move' (загальний випадок)
        case ["move", x, y]:
            return f"Рух до: ({x}, {y})"
        # 3. Команда 'attack' на дракона (використовуємо 'if' умову)
        case ["attack", target] if target == "dragon":
            return "Критична атака на дракона!"
        # 4. Команда 'attack' (загальний випадок)
        case ["attack", target]:
            return f"Атака на {target}"
        # 5. Невідома команда
        case _:
            return "Невірна команда."
        
# test
print(f"Command 1: {process_game_command(["move", 5, 5])}")
print(f"Command 2: {process_game_command(["move", 3, 7])}")
print(f"Command 3: {process_game_command(["attack", "dragon"])}")
print(f"Command 4: {process_game_command(["attack", "goblin"])}")
print(f"Command 5: {process_game_command(["heal", 100])}")
