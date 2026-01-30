import os
from dotenv import load_dotenv

# Завантажуємо .env
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # Заміни 'password' на свій справжній пароль від MySQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                            'mysql+pymysql://root:Password@127.0.0.1/my_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Знаходимо корінь проекту (на рівень вище від backend)
    # Тепер шлях буде точно в твою папку media
    UPLOAD_FOLDER = os.path.abspath(os.path.join(basedir, '..', 'media'))