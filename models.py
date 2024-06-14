from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    ingredients_file = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.image_file}')"
