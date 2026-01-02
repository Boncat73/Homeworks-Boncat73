from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'super-secret-key-123'  # Це потрібно для роботи flash

@app.route('/', methods=['GET', 'POST'])
def index():
    user_info = {
        "name": "Василь!",
        "role": "Python Developer",
        "bio": "Створюю будь-що, будь-де, будь-коли, для тих, хто потребує)",
        "skills": ["Python", "Flask", "SQL", "HTML/CSS", "Other..."]
    }

    if request.method == 'POST':
        name = request.form.get('name')
        # Логіка обробки (наприклад, запис у файл або консоль)
        print(f"Повідомлення від {name}")

        # Створюємо flash-повідомлення
        flash(f"Дякую, {name}! Ваше повідомлення успішно надіслано.", "success")
        
        # Перенаправляємо назад на головну, щоб форма очистилася
        return redirect(url_for('index'))

    return render_template('index.html', user=user_info)

if __name__ == '__main__':
    app.run(debug=True)