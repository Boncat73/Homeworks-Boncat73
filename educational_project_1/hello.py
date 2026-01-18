from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# маршрут для головної сторінки з логіном
@app.route('/', methods=['GET', 'POST'])
def login_page():  # змінив назву з index на login_page, щоб не було конфлікту
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'bonvas73@gmail.com' and password == '23051973':
            return redirect(url_for('dashboard'))
        else:
            error = "Невірний логін або пароль!"
            
    return render_template('login.html', error=error)

# маршрут для сторінки після успішного входу
@app.route('/dashboard')
def dashboard():
    return "Вітаємо на Dashboard! Ви успішно увійшли."

# маршрут для головної сторінки
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # використовуємо 5001, щоб оминути системну службу macOS
    app.run(port=5001, debug=True)

