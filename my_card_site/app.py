import os # модуль для роботи з операційною системою (шляхи до файлів)
from flask import Flask, render_template, request, flash, redirect, url_for, session # основні інструменти Flask
from flask_sqlalchemy import SQLAlchemy # бібліотека для роботи з базами даних
from datetime import datetime # бібліотека для роботи з датами та часом

app = Flask(__name__) # створюємо екземпляр додатка Flask

# секретний ключ потрібен для роботи сесій (авторизації адміна у даному випадку)
# coocies працюють неявно через обʼєкт session. Flask бере дані,
# які кладуться у цей обʼєкт,підписує ключем та відправляє у браузер користувача як куку
app.secret_key = 'super-secret-key-123'

# налаштування бази даних SQLite
# визначаємо шлях до папки, де лежить цей файл (app.py)
basedir = os.path.abspath(os.path.dirname(__file__))
# вказуємо Flask, де саме створювати файл бази даних messages.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'messages.db')
# вимикаємо зайві сповіщення від SQLAlchemy для економії ресурсів
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # ініціалізуємо базу даних, прив'язуючи її до нашого додатка

# пароль для входу в адмін-панель
ADMIN_PASSWORD = 'Bn09091973Bn'

# модель даних
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True) # унікальний номер кожного повідомлення
    name = db.Column(db.String(50), nullable=False) # ім'я відправника (макс. 50 символів)
    email = db.Column(db.String(50), nullable=False) # електронна пошта
    text = db.Column(db.Text, nullable=False) # текст повідомлення
    date_sent = db.Column(db.DateTime, default=datetime.utcnow) # автоматична дата відправки (UTC)

# створюємо таблиці в базі даних автоматично при запуску, якщо їх ще немає
with app.app_context():
    db.create_all()

# маршрути для користувача
@app.route('/', methods=['GET', 'POST'])
def index():
# дані про власника сайту з відображенням у шаблоні
    user_info = {
        "name": "Василь",
        "role": "Python Developer",
        "bio": "Створюю будь-що, будь-де, будь-коли для тих, хто потребує.",
        "skills": ["Python", "Flask", "SQLite", "JavaScript", "HTML/CSS", "Git"]
    }

    if request.method == 'POST': # якщо юзер натиснув кнопку "Надіслати"
        name = request.form.get('name') # беремо імʼя з поля форми
        email = request.form.get('email') # беремо email з поля форми
        message_text = request.form.get('message') # беремо текст повідомлення

        try:
            # створюємо новий об'єкт повідомлення на основі моделі
            new_msg = Message(name=name, email=email, text=message_text)
            db.session.add(new_msg) # додаємо його в чергу на запис
            db.session.commit() # зберігаємо зміни в самому файлі .db
            flash(f"Дякую, {name}! Ваше повідомлення збережено.", "success")
        except Exception as e:
            flash(f"Помилка бази даних: {e}", "danger") # якщо щось пішло не так
        
        return redirect(url_for('index')) # перезавантажуємо сторінку після відправки

    # якщо просто відкрили сайт (GET) — показуємо головну сторінку з даними user_info
    return render_template('index.html', user=user_info)

# маршрути авторізаці
@app.route('/login', methods=['GET', 'POST']) # сторінка для входу для адміна
def login():
    if request.method == 'POST':
        entered_password = request.form.get('password') # отримуємо пароль з форми
        if entered_password == ADMIN_PASSWORD: # перевіряємо, чи збігається він з константою
            session['logged_in'] = True # записуємо в сесію браузера, що вхід успішний
            flash("Ви успішно увійшли до панелі керування!", "success")
            return redirect(url_for('admin')) # пускаємо в адмінку
        else:
            flash("Невірний пароль! Спробуйте ще раз.", "danger")
    return render_template('login.html') # якщо метод GET — показуємо форму входу

@app.route('/logout') # вихід з облікового запису
def logout():
    session.pop('logged_in', None) # видаляємо ключ авторизації ші сесії
    flash("Ви вийшли із системи.", "info")
    return redirect(url_for('index')) # повертаємо на головну сторінку

# маршрути адміністратора(захищені CRUD)
@app.route('/admin') # сторінка перегляду всіх повідомлень (метод READ)
def admin():
    if not session.get('logged_in'): # якщо не авторизований — виганяємо на вхід
        return redirect(url_for('login'))
    
    # отримуємо всі записи з бази, сортуючи їх так, щоб нові були зверху
    all_messages = Message.query.order_by(Message.date_sent.desc()).all()
    return render_template('admin.html', messages=all_messages)

@app.route('/edit/<int:id>', methods=['GET', 'POST']) # редагування повідомлення (метод UPDATE)
def edit_message(id):
    if not session.get('logged_in'): # захист доступу
        return redirect(url_for('login'))
        
    msg = Message.query.get_or_404(id) # знаходимо запис за ID або видаємо помилку 404
    
    if request.method == 'POST':
        # оновлюємо поля існуючого об'єкта новими даними з форми
        msg.name = request.form.get('name')
        msg.email = request.form.get('email')
        msg.text = request.form.get('message')
        
        try:
            db.session.commit() # зберігаємо оновлені дані
            flash("Повідомлення успішно оновлено!", "success")
            return redirect(url_for('admin'))
        except Exception as e:
            flash(f"Помилка при оновленні: {e}", "danger")
    
    # показуємо форму редагування з уже заповненими старими даними
    return render_template('edit.html', message=msg)

@app.route('/delete/<int:id>') # видалення повідомлення (метод DELETE)
def delete_message(id):
    if not session.get('logged_in'): # захист доступу
        return redirect(url_for('login'))
        
    message_to_delete = Message.query.get_or_404(id) # шукаємо об'єкт в базі
    try:
        db.session.delete(message_to_delete) # видаляємо його з черги
        db.session.commit() # підтверджуємо видалення в базі
        flash("Повідомлення видалено успішно!", "success")
    except Exception as e:
        flash(f"Не вдалося видалити: {e}", "danger")
    
    return redirect(url_for('admin'))  # повертаємося до списку повідомлень

# точка входу: запускати сервер, тільки якщо файл запущений як основний
if __name__ == '__main__':
    # Режим налагодження (debug=True) дозволяє бачити помилки та авто-оновлювати сайт
    app.run(debug=True)