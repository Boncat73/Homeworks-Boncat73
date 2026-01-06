import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# Секретний ключ потрібен для роботи сесій (авторизації)
app.secret_key = 'super-secret-key-123'

# Налаштування бази даних SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'messages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Пароль для входу в адмін-панель
ADMIN_PASSWORD = 'Bn09091973Bn'  # Зміни на свій

# --- МОДЕЛЬ ДАНИХ ---
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

# Створення бази даних
with app.app_context():
    db.create_all()

# --- МАРШРУТИ КОРИСТУВАЧА ---

@app.route('/', methods=['GET', 'POST'])
def index():
    user_info = {
        "name": "Василь",
        "role": "Python Developer",
        "bio": "Створюю будь-що, будь-де, будь-коли для тих, хто потребує.",
        "skills": ["Python", "Flask", "SQLite", "JavaScript", "HTML/CSS", "Git"]
    }

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_text = request.form.get('message')

        try:
            new_msg = Message(name=name, email=email, text=message_text)
            db.session.add(new_msg)
            db.session.commit()
            flash(f"Дякую, {name}! Ваше повідомлення збережено.", "success")
        except Exception as e:
            flash(f"Помилка бази даних: {e}", "danger")
        
        return redirect(url_for('index'))

    return render_template('index.html', user=user_info)

# --- МАРШРУТИ АВТОРИЗАЦІЇ ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        entered_password = request.form.get('password')
        if entered_password == ADMIN_PASSWORD:
            session['logged_in'] = True
            flash("Ви успішно увійшли до панелі керування!", "success")
            return redirect(url_for('admin'))
        else:
            flash("Невірний пароль! Спробуйте ще раз.", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Ви вийшли із системи.", "info")
    return redirect(url_for('index'))

# --- МАРШРУТИ АДМІНІСТРАТОРА (ЗАХИЩЕНІ CRUD) ---

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    all_messages = Message.query.order_by(Message.date_sent.desc()).all()
    return render_template('admin.html', messages=all_messages)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_message(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    msg = Message.query.get_or_404(id)
    
    if request.method == 'POST':
        msg.name = request.form.get('name')
        msg.email = request.form.get('email')
        msg.text = request.form.get('message')
        
        try:
            db.session.commit()
            flash("Повідомлення успішно оновлено!", "success")
            return redirect(url_for('admin'))
        except Exception as e:
            flash(f"Помилка при оновленні: {e}", "danger")
    
    return render_template('edit.html', message=msg)

@app.route('/delete/<int:id>')
def delete_message(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    message_to_delete = Message.query.get_or_404(id)
    try:
        db.session.delete(message_to_delete)
        db.session.commit()
        flash("Повідомлення видалено успішно!", "success")
    except Exception as e:
        flash(f"Не вдалося видалити: {e}", "danger")
    
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)