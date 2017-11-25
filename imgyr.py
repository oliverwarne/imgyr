from PIL import Image 

import flask
import os
import uuid

from werkzeug.utils import secure_filename

app = flask.Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Some constants. Probably don't change these. You can if you want. I'm not your boss
MAX_WIDTH  = 500
MAX_HEIGHT = 500
size = 500,500

FOLDER = "storage/"
EXTENSIONS = ["png", "jpg", "jpeg"]

@app.route("/")
def home():
    return flask.render_template("what.html")

@app.route("/what")
def what():
    return flask.render_template("what.html")

@app.route("/view/<filename>")
def view(filename):
    return flask.send_from_directory(FOLDER, filename)

@app.route("/upload")
def naughty():
    return flask.render_template("error.html",message="You sure you uploaded a file?")

@app.route("/upload", methods=["POST"])
@app.route("/", methods=["POST"])
def upload():
    request = flask.request
    file = request.files['file']
    if not file:
        print("wotsir")
        return flask.render_template("error.html",message="You sure you uploaded a file?")
    if  not allowed_file(file.filename):
        print("wotsir")
        return flask.render_template("error.html", message="Use png or jpeg")

    ext = os.path.splitext(file.filename)[1].lower()
    filename = generate_name() + ext
    filename = secure_filename(filename)
    """
    pic = file.read()
    width, height = pic.size

    if width > MAX_WIDTH or height > MAX_HEIGHT:
        print("wotsir")
        return flask.render_template("error.html", message="bigboi")
    """
    file.save(os.path.join(FOLDER, filename))
    print("wotsir")

    return flask.redirect(flask.url_for("view", filename=filename))
"""
    request = flask.request
    print("s'gucciii")
    if request.method == 'POST':
        # check if the post request has the file part
        file.filename = 
        if 'file' not in request.files:
            print("s'gucciiiiia")
            print("ookay")
            return flask.redirect(request.url)
        file = request.files['file']
        print("s'gucciiri")
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            print("s'guccrriii")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print("s'gucciirrrrrai")
            print("s'gucci")
            filename = secure_filename(file.filename)
            file.save(os.path.join(FOLDER, filename))
            return flask.redirect(flask.url_for('view',
                                    filename=filename))
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
            <p><input type=file name=file>
                <input type=submit value=Upload>
        </form>
        '''

"""

def allowed_file(filename):
    print(filename)
    print(filename.rsplit('.', 1)[1].lower())
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in EXTENSIONS

def generate_name() -> str:
    return str(uuid.uuid4())[0:6]

if __name__ == "__main__":
    app.run(debug=False)
