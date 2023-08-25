from flask import Flask, url_for, request, render_template, jsonify, flash
import tensorflow as tf
from tensorflow import keras
from werkzeug.utils import secure_filename
import os
import numpy as np

app = Flask(__name__)

# Load your model here

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        f = request.files['file']
        #f.save('uploaded_files/'+ secure_filename(f.filename))
        f.save(secure_filename(f.filename))

        # do prediction here using the uploaded file at:
        # 'uploaded_files/'+ secure_filename(f.filename)
        
        result_string="test"

        return render_template('index.html', prediction_text='The predictions are: {}'.format(result_string))



if __name__ == '__main__':
    app.run()
