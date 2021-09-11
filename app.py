from flask import Flask, render_template, request
from db import *
import os
os.chdir(__file__.replace(os.path.basename(__file__), ''))
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello', methods=['POST'])
def hello():
    var_name = request.form['name']
    var_age = request.form['age']
    image = request.files['image']
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'static/image1.jpg'))
    addEntry(var_name, var_age)  
    return render_template("hello.html", na=var_name, ag=var_age)

@app.route('/search')
def search():
    imagePaths = ["../static/image1.jpg"]
    return render_template("search.html", result=show(), imagepaths=imagePaths)

if __name__ == '__main__':
    app.run()