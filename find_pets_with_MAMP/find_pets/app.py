import os
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'pet_finder_super_secret_key'

# --- НАЛАШТУВАННЯ ЗАВАНТАЖЕНЬ ---
# Вказуємо шлях до папки uploads на флешці
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Обмеження розміру файлу (напр. 5 МБ)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 

# --- НАЛАШТУВАННЯ БАЗИ ДАНИХ MAMP ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:8889/find_pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- МОДЕЛІ ДАНИХ ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    pets = db.relationship('Pet', backref='author', lazy=True)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100), nullable=True) # Поле для назви фото
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# --- МАРШРУТИ ---

# 1. Головна сторінка (Read)
@app.route('/')
def index():
    all_pets = Pet.query.order_by(Pet.id.desc()).all()
    return render_template('index.html', pets=all_pets)

# 2. Реєстрація (Create User)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_pw = generate_password_hash(request.form['password'])
        new_user = User(username=request.form['username'], password=hashed_pw)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return "Цей логін вже зайнятий! <a href='/register'>Спробувати інший</a>"
    return render_template('register.html')

# 3. Вхід (Auth)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            return redirect(url_for('index'))
        return "Невірний логін або пароль! <a href='/login'>Спробувати ще раз</a>"
    return render_template('login.html')

# 4. Додавання оголошення (Create Pet + Upload)
@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        file = request.files.get('photo')
        filename = None
        
        # Обробка завантаження файлу
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        new_pet = Pet(
            title=request.form['title'],
            description=request.form['description'],
            contact_info=request.form['contact'],
            image_file=filename,
            user_id=session['user_id']
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_pet.html')

# 5. Видалення (Delete - тільки адмін)
@app.route('/admin/delete/<int:id>')
def delete_pet(id):
    if not session.get('is_admin'):
        return "Доступ заборонено!", 403
    pet = Pet.query.get_or_404(id)
    
    # Видаляємо фізичний файл фото, якщо він є
    if pet.image_file:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], pet.image_file))
        except:
            pass # Якщо файл вже видалений вручну
            
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('index'))

# 6. Вихід
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# --- ЗАПУСК ---
if __name__ == '__main__':
    with app.app_context():
        # Створюємо таблиці, якщо їх ще немає
        db.create_all()
    app.run(debug=True)