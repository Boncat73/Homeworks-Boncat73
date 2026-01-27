from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1. КОНФІГУРАЦІЯ БАЗИ ДАНИХ
# mysql+pymysql://користувач:пароль@хост/назва_бази
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Password@localhost/homework_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Секретний ключ потрібен для безпечної роботи сесій (якщо захочете додати flash-повідомлення)
app.secret_key = 'super_secret_key'

# 2. ІНІЦІАЛІЗАЦІЯ SQLAlchemy
db = SQLAlchemy(app)

# 3. МОДЕЛЬ ТАБЛИЦІ (Об'єктно-реляційне відображення - ORM)
class Student(db.Model):
    # Визначаємо структуру таблиці 'student' у MySQL
    id = db.Column(db.Integer, primary_key=True)      # Первинний ключ (унікальний для кожного)
    name = db.Column(db.String(100), nullable=False)  # Текстове поле (не може бути порожнім)
    grade = db.Column(db.Integer)                     # Числове поле для оцінки

    def __repr__(self):
        # Як об'єкт буде відображатися при друку в консолі
        return f'<Student {self.name}>'

# 4. МАРШРУТИ (ROUTES)

# Головна сторінка: Читання (Read)
@app.route('/')
def index():
    # Робимо запит: SELECT * FROM student ORDER BY id DESC
    # .order_by(Student.id.desc()) дозволяє бачити нові записи першими
    students = Student.query.order_by(Student.id.desc()).all()
    return render_template('index.html', students=students)

# Додавання студента: Створення (Create)
@app.route('/add', methods=['POST'])
def add_student():
    # Отримуємо дані з форми HTML (атрибут 'name' у тегах <input>)
    name_from_form = request.form.get('student_name')
    grade_from_form = request.form.get('student_grade')

    if name_from_form:
        try:
            # Створюємо новий екземпляр класу Student
            new_student = Student(
                name=name_from_form, 
                grade=int(grade_from_form) if grade_from_form else 0
            )
            # Додаємо об'єкт у сесію (підготовка до запису)
            db.session.add(new_student)
            # Фіксуємо зміни в базі даних (COMMIT)
            db.session.commit()
        except Exception as e:
            # Якщо щось пішло не так (наприклад, база відключилася)
            db.session.rollback() # Скасовуємо зміни, щоб не "зламати" базу
            print(f"Помилка при збереженні: {e}")
    
    return redirect(url_for('index'))

# Видалення студента: Видалення (Delete)
@app.route('/delete/<int:id>')
def delete_student(id):
    # Знаходимо студента за ID або видаємо помилку 404, якщо його немає
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student) # Помічаємо об'єкт на видалення
        db.session.commit()        # Виконуємо DELETE в MySQL
    except Exception as e:
        db.session.rollback()
        print(f"Помилка при видаленні: {e}")
    
    return redirect(url_for('index'))

# 5. ЗАПУСК ПРОГРАМИ
if __name__ == '__main__':
    # Створюємо контекст програми для роботи з БД поза запитами
    with app.app_context():
        # Створює таблиці в MySQL на основі класів (якщо їх ще немає)
        # Це автоматично виконає SQL команду CREATE TABLE IF NOT EXISTS
        db.create_all()
        print("--- Зв'язок з MySQL встановлено, таблиці готові! ---")

    # debug=True дозволяє серверу перезавантажуватися при зміні коду
    app.run(debug=True)