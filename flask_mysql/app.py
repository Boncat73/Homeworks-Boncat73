from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# --- КОНФІГУРАЦІЯ БАЗИ ДАНИХ ---
# mysql+pymysql://користувач:пароль@хост/назва_бази
# Замініть 'Password123!' на ваш реальний пароль, який ви вказали в системі
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password@localhost/homework_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Створюємо об'єкт бази даних
db = SQLAlchemy(app)

# --- МОДЕЛЬ ТАБЛИЦІ ---
# Це опис того, як виглядає таблиця в MySQL
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Унікальний ID
    name = db.Column(db.String(100), nullable=False)  # Ім'я (текст до 100 симв.)
    grade = db.Column(db.Integer)  # Оцінка (ціле число)

    def __repr__(self):
        return f'<Student {self.name}>'

# --- МАРШРУТИ (ROUTES) ---

# Головна сторінка: показує список усіх студентів
@app.route('/')
def index():
    # Отримуємо всіх студентів із бази даних (SELECT * FROM student)
    students = Student.query.all()
    return render_template('index.html', students=students)

# Маршрут для додавання нового студента через форму
@app.route('/add', methods=['POST'])
def add_student():
    # Отримуємо дані з полів форми в HTML
    name_from_form = request.form.get('student_name')
    grade_from_form = request.form.get('student_grade')

    if name_from_form:
        # Створюємо новий об'єкт студента
        new_student = Student(name=name_from_form, grade=grade_from_form)
        # Додаємо його в сесію бази даних
        db.session.add(new_student)
        # Зберігаємо зміни в MySQL (COMMIT)
        db.session.commit()
    
    # Повертаємося на головну сторінку, щоб побачити оновлений список
    return redirect(url_for('index'))

# --- ЗАПУСК ТА АВТОМАТИЧНЕ СТВОРЕННЯ БАЗИ ---
if __name__ == '__main__':
    with app.app_context():
        # Створює таблиці в MySQL, якщо їх ще не існує
        db.create_all()
        print("База даних підключена, таблиці перевірено.")

    # Запуск в режимі розробки
    app.run(debug=True)