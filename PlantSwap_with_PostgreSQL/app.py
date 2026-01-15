from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Налаштування підключення до PostgreSQL
# Якщо у вас встановлено пароль, замініть на: 'postgresql://postgres:пароль@localhost:5432/plantswap_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/plantswap_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- МОДЕЛЬ ДАНИХ ---
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100))
    category = db.Column(db.String(50), default='Кімнатна')  # Наш поділ на типи
    status = db.Column(db.String(50), default='Доступно')    # Доступно, Заброньовано, Обміняно
    description = db.Column(db.Text)
    care_instructions = db.Column(db.Text)

    def __repr__(self):
        return f'<Plant {self.name}>'

# Створення таблиць (виконується один раз)
with app.app_context():
    db.create_all()

# --- МАРШРУТИ ДЛЯ КОРИСТУВАЧА ---

@app.route('/')
def index():
    # Отримуємо категорію з URL-параметра (наприклад, /?cat=Сукулент)
    cat = request.args.get('cat')
    if cat:
        plants = Plant.query.filter_by(category=cat).order_by(Plant.id.desc()).all()
    else:
        plants = Plant.query.order_by(Plant.id.desc()).all()
    return render_template('index.html', plants=plants)

# --- МАРШРУТИ ДЛЯ АДМІНІСТРАТОРА ---

@app.route('/admin')
def admin_panel():
    plants = Plant.query.order_by(Plant.id).all()
    return render_template('admin.html', plants=plants)

# Додавання нової рослини
@app.route('/plant/add', methods=['POST'])
def add_plant():
    new_plant = Plant(
        name=request.form.get('name'),
        species=request.form.get('species'),
        category=request.form.get('category'),
        description=request.form.get('description'),
        status='Доступно'
    )
    db.session.add(new_plant)
    db.session.commit()
    return redirect(url_for('admin_panel'))

# Сторінка повного редагування
@app.route('/plant/edit/<int:id>')
def edit_plant_page(id):
    plant = Plant.query.get_or_404(id)
    return render_template('edit.html', plant=plant)

# Обробка повного оновлення (UPDATE)
@app.route('/plant/update/<int:id>', methods=['POST'])
def update_plant(id):
    plant = Plant.query.get_or_404(id)
    plant.name = request.form.get('name')
    plant.species = request.form.get('species')
    plant.category = request.form.get('category')
    plant.status = request.form.get('status')
    plant.description = request.form.get('description')
    plant.care_instructions = request.form.get('care_instructions')
    
    db.session.commit()
    return redirect(url_for('admin_panel'))

# Швидке оновлення статусу (PATCH-like)
@app.route('/plant/patch/<int:id>', methods=['POST'])
def patch_plant(id):
    plant = Plant.query.get_or_404(id)
    plant.status = request.form.get('status')
    db.session.commit()
    return redirect(url_for('admin_panel'))

# Видалення рослини (DELETE)
@app.route('/plant/delete/<int:id>', methods=['POST'])
def delete_plant(id):
    plant = Plant.query.get_or_404(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('admin_panel'))

# --- ЗАПУСК СЕРВЕРА ---
if __name__ == '__main__':
    # Використовуємо порт 8000, щоб уникнути конфліктів AirPlay на macOS
    app.run(debug=True, port=8000)