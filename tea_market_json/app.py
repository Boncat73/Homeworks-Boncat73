import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = 'data.json'

# функції для роботи з JSON 
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# маршрути

# головна сторінка
@app.route('/')
def index():
    teas = load_data()
    return render_template('index.html', teas=teas)

# сторінка адміна
@app.route('/admin')
def admin():
    teas = load_data()
    return render_template('admin.html', teas=teas)

# додавання товару
@app.route('/add', methods=['POST'])
def add_tea():
    teas = load_data()
    new_tea = {
        "id": len(teas) + 1,
        "name": request.form['name'],
        "sku": request.form['sku'],
        "weight": int(request.form['weight']),
        "type": request.form['type'],
        "price_retail": float(request.form['price_retail']),
        "price_wholesale": float(request.form['price_wholesale'])
    }
    teas.append(new_tea)
    save_data(teas)
    return redirect(url_for('admin'))

# видалення товару
@app.route('/delete/<int:tea_id>')
def delete_tea(tea_id):
    teas = load_data()
    teas = [t for t in teas if t['id'] != tea_id]
    save_data(teas)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)