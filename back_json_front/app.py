from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# Підключення до твоєї створеної бази
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:пароль@localhost/my_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    city = db.Column(db.String(100))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# МАРШРУТ ДЛЯ РЕЄСТРАЦІЇ (POST)
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    try:
        new_user = User(
            username=data['username'],
            email=data['email'],
            password=hashed_password,
            age=data['age'],
            city=data['city']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Користувача додано успішно!"}), 201
    except Exception:
        return jsonify({"error": "Помилка! Можливо, email вже існує."}), 400

# МАРШРУТ ДЛЯ ОТРИМАННЯ СПИСКУ (GET)
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{"username": u.username, "age": u.age, "city": u.city} for u in users]
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(debug=True)