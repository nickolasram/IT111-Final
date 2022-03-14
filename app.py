from flask import Flask, render_template, session, redirect, flash, request, send_from_directory
from user_file.user_file import User_file
from second import second
from databaseconfig import repo, filecol, usercol

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
app.register_blueprint(second, url_prefix="/user")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['UPLOAD_FOLDER'] = repo
app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)
app.add_url_rule(
    "/user/<user>", endpoint="user_profile", build_only=True
)

ALLOWED_EXTENSIONS = {'txt'}


def allowed_file(filename):
  return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
  if 'logged_in' in session:
    return redirect("/dashboard/")
  else:
    return redirect('/login/')


@app.route('/login/')
def login():
  return render_template('login.html')

@app.route('/uploadfile/', methods=['GET', 'POST'])
def uploadfile():
  if request.method == 'POST':
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      return User_file.upload(User_file, file)
  return render_template('upload.html')


@app.route('/dashboard/')
def dashboard():
  files = filecol.find({})
  users = usercol.find({})
  return render_template('dashboard.html', files=files, users=users, user=session['user']['name'])


@app.route('/uploads/<name>')
def download_file(name):
  return send_from_directory(app.config["UPLOAD_FOLDER"], name)


@app.route('/user/<user>')
def user_profile(user):
  user_record = filecol.find({"name": user})
  return render_template('profile.html', user_record=user_record)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)














