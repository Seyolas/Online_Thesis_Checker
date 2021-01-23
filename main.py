import os
from flask import Flask, render_template, flash, redirect, url_for, request,session,send_file
from werkzeug.utils import secure_filename
from docx import document
import algoritmalar as backend

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cairocoders-ednalan'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 64 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['docx']) # izin verilen dosya türleri


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['inputFile']
        if file and allowed_file(file.filename):
            secfil = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secfil))
            flash('Dosyanız başarıyla yüklendi! ' + file.filename)
            newfilename = backend.process(os.path.join(app.config['UPLOAD_FOLDER'], secfil))
            return send_file(newfilename)
        else:
            flash('Sadece docx uzantılı dosya yükleyiniz!')
        return redirect('/')

if __name__ == '__main__':
    app.run()