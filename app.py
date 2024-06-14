from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'image' not in request.files or 'ingredients' not in request.files:
            flash('No file part')
            return redirect(request.url)
        image = request.files['image']
        ingredients = request.files['ingredients']
        if image.filename == '' or ingredients.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if image and allowed_file(image.filename) and ingredients and allowed_file(ingredients.filename):
            image_filename = secure_filename(image.filename)
            ingredients_filename = secure_filename(ingredients.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            ingredients.save(os.path.join(app.config['UPLOAD_FOLDER'], ingredients_filename))
            product = Product(name=request.form['name'],
                              description=request.form['description'],
                              image_file=image_filename,
                              ingredients_file=ingredients_filename)
            db.session.add(product)
            db.session.commit()
            flash('File(s) successfully uploaded')
            return redirect(url_for('upload_file'))
    return render_template('upload.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
