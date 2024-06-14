import os

class Config:
    SECRET_KEY = 'c4826295924d4175419a2e34dcd38d0b'  # Ersätt med din genererade nyckel
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Max 16MB file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
