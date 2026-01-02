from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_info = {
        "name": "Василь!",
        "role": "Python Developer",
        "bio": "Створюю будь-що, будь-де, будь-коли, для тих, хто потребує)",
        "skills": ["Python", "Flask", "SQL", "HTML/CSS", "Other..."]
    }

    if request.method == 'POST':
        # Отримуємо дані з форми
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"Нове повідомлення від {name} ({email}): {message}")
        # Тут можна додати логіку збереження в базу або відправки на email
        
        return f"<h1>Дякую, {name}! Ваше повідомлення отримано.</h1><a href='/'>Назад</a>"

    return render_template('index.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)