from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'#потрібно для роботи flash-повідомлень

# Додаємо маршрут для головної сторінки
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm', '').strip() # Отримуємо ім'я та видаляємо пробіли
        
        if not user: # Перевірка: якщо рядок порожній
            flash("Будь ласка, введіть ваше ім'я!")
            return redirect(url_for('index'))
            
        return redirect(url_for('success', name=user))
    return redirect(url_for('index'))

@app.route('/success/<name>')
def success(name):
    return render_template('welcome.html', user_name=name)
    

# @app.route("/")
# def index():
#     return "<h1>Заголовок h1</h1>"

# @app.route("/contacts")
# def contacts():
#     return "contacts"

# @app.route("/about")
# def about():
#     return "about"

# приклад як на один і той же обробник "вішати" 
# кілька URL:
# @app.route("/index")

# @app.route("/about")
# def about():
#     return "<h1>About Us</h1>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

# from markupsafe import escape

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"



