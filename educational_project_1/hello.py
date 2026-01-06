from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Маршрут для головної сторінки з логіном
@app.route('/', methods=['GET', 'POST'])
def login_page():  # Змінив назву з index на login_page, щоб не було конфлікту
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'bonvas73@gmail.com' and password == 'qwert':
            return redirect(url_for('dashboard'))
        else:
            error = "Невірний логін або пароль!"
            
    return render_template('login.html', error=error)

# Маршрут для сторінки після успішного входу
@app.route('/dashboard')
def dashboard():
    return "Вітаємо на Dashboard! Ви успішно увійшли."

if __name__ == '__main__':
    # Використовуємо 5001, щоб оминути системну службу macOS
    app.run(port=5001, debug=True)

