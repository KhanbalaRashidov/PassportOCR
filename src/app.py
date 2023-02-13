import base64
from werkzeug.utils import secure_filename
from flask_cors import CORS
from flask import Flask, flash, request, redirect, url_for, render_template
import os
import passport
app = Flask(__name__, template_folder='templates')
CORS(app)

UPLOAD_FOLDER = "./static/uploads/"
# create this path if not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
app.secret_key = "secret key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def get_recognition():
    return render_template("index.html")

@app.route('/ocr', methods=['POST'])
def ocr():
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    files = request.files.getlist("file")
    file_names = []
    encodings = []
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file_names.append(file_path)
            file.save(file_path)
            encodings.append(file_path)

        else:
            flash('Allowed image types are -> png, jpg, jpeg, gif')
            return redirect(request.url)

    with open(file_names[0], "rb") as image_file:
        data = base64.standard_b64encode(image_file.read())
    
    personInfo= passport.getPaasportText(img=file_names[0])
    os.remove(file_names[0])
    return {
        "data": personInfo,
        #"image": "data:image/jpg;base64," + data.decode('utf-8')
    }

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5002)