from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'#потрібно для роботи flash-повідомлень

# Додаємо маршрут для головної сторінки
@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        # Отримуємо дані з полів форми
        username = request.form.get('username')
        password = request.form.get('password')

        # Проста перевірка (логін: bonvas73@gmail.com, пароль: qwert)
        if username == 'bonvas73@gmail.com' and password == 'qwert':
            return redirect(url_for('dashboard')) # Тут може бути redirect на іншу сторінку
        else:
            error = "Невірний логін або пароль!"
            
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route("/contacts")
def contacts():
    return "contacts"

@app.route("/about")
def about():
    return "about"

@app.route("/welcome")
def welcome():
    return "welcome"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

