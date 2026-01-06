import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key-123'

# налаштування бази даних SQLite
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'messages.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# модель повідомлення (таблиця в базі)
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

# створення бази даних (якщо її ще немає)
with app.app_context():
    db.create_all()

# маршрути

@app.route('/', methods=['GET', 'POST'])
def index():
    # інформація про адміна (dictionary and list)
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

        # збереження в базу 
        try:
            new_msg = Message(name=name, email=email, text=message_text)
            db.session.add(new_msg)
            db.session.commit()
            flash(f"Дякую, {name}! Ваше повідомлення збережено.", "success")
        except Exception as e:
            flash(f"Помилка бази даних: {e}", "danger")
        
        return redirect(url_for('index'))

    return render_template('index.html', user=user_info)

@app.route('/admin')
def admin():
    # отримую усі повідомлення, нові зверху
    all_messages = Message.query.order_by(Message.date_sent.desc()).all()
    return render_template('admin.html', messages=all_messages)

@app.route('/delete/<int:id>')
def delete_message(id):
    # пошук повідомлення за id
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