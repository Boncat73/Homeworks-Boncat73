import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, MediaFile

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

@app.route('/api/status')
def status():
    return jsonify({"status": "Бекенд працює на порту 5001"})

@app.route('/api/media', methods=['GET'])
def get_media():
    files = MediaFile.query.all()
    # Додаємо ID, щоб фронтенд знав, що саме видаляти
    return jsonify([{"id": f.id, "name": f.filename, "type": f.file_type} for f in files])

@app.route('/api/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "Файл не отримано"}), 400
    
    file = request.files['file']
    f_type = request.form.get('type', 'photos')
    
    if file:
        from werkzeug.utils import secure_filename
        filename = secure_filename(file.filename)
        target_dir = os.path.join(app.config['UPLOAD_FOLDER'], f_type)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        save_path = os.path.join(target_dir, filename)
        file.save(save_path)
        
        new_entry = MediaFile(filename=filename, file_type=f_type)
        db.session.add(new_entry)
        db.session.commit()
        
        return jsonify({"message": "Збережено успішно!"}), 201

# --- НОВИЙ МАРШРУТ ДЛЯ ВИДАЛЕННЯ ---
@app.route('/api/delete/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
    file_record = MediaFile.query.get(file_id)
    if not file_record:
        return jsonify({"error": "Файл не знайдено в базі"}), 404

    # Шлях до файлу на диску
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_record.file_type, file_record.filename)

    try:
        # 1. Видаляємо фізичний файл, якщо він існує
        if os.path.exists(file_path):
            os.remove(file_path)
        
        # 2. Видаляємо запис із бази даних
        db.session.delete(file_record)
        db.session.commit()
        
        return jsonify({"message": "Файл успішно видалено"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)