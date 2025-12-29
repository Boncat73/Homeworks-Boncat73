from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

# Додаємо маршрут для головної сторінки
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    return 'Welcome , %s!' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
    

# @app.route("/")
# def index():
#     return "<h1>Заголовок h1</h1>"

# @app.route("/contacts")
# def contacts():
#     return "contacts"

# @app.route("/about")
# def about():
#     return "about"

# приклад як на один і той же обробник "вішати" 
# кілька URL:
# @app.route("/index")

# @app.route("/about")
# def about():
#     return "<h1>About Us</h1>"

if __name__ == "__main__":
    app.run(port=5000, debug=True)

# from markupsafe import escape

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"



