from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# конфігурація бази даних
# mysql+pymysql://користувач:пароль@хост/назва_бази
# Password - реальний пароль
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password@localhost/homework_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# створюємо об'єкт бази даних
db = SQLAlchemy(app)

# модель таблиці
# це опис того, як виглядає таблиця в MySQL
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # унікальний ID
    name = db.Column(db.String(100), nullable=False)  # ім'я (текст до 100 симв.)
    grade = db.Column(db.Integer)  # оцінка (ціле число)

    def __repr__(self):
        return f'<Student {self.name}>'

# маршрути (ROUTES)

# Головна сторінка: показує список усіх студентів
@app.route('/')
def index():
    # отримуємо всіх студентів із бази даних (SELECT * FROM student)
    students = Student.query.all()
    return render_template('index.html', students=students)

# маршрут для додавання нового студента через форму
@app.route('/add', methods=['POST'])
def add_student():
    # отримуємо дані з полів форми в HTML
    name_from_form = request.form.get('student_name')
    grade_from_form = request.form.get('student_grade')

    if name_from_form:
        # створюємо новий об'єкт студента
        new_student = Student(name=name_from_form, grade=grade_from_form)
        # додаємо його в сесію бази даних
        db.session.add(new_student)
        # зберігаємо зміни в MySQL (COMMIT)
        db.session.commit()
    
    # повертаємося на головну сторінку, щоб побачити оновлений список
    return redirect(url_for('index'))

# запуск та автоматичне створення бази
if __name__ == '__main__':
    with app.app_context():
        # створює таблиці в MySQL, якщо їх ще не існує
        db.create_all()
        print("База даних підключена, таблиці перевірено.")

    # запуск в режимі розробки
    app.run(debug=True)