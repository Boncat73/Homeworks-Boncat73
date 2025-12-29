from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/contacts")
def contacts():
    return "contacts"

@app.route("/about")
def about():
    return "about"

# приклад як на один і той же обробник "вішати" 
# кілька URL:
# @app.route("/index")

# @app.route("/about")
# def about():
#     return "<h1>About Us</h1>"

if __name__ == "__main__":
    app.run(port=5001, debug=True)

# from markupsafe import escape

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/hello")
# def hello():
#     name = request.args.get("name", "Flask")
#     return f"Hello, {escape(name)}!"



