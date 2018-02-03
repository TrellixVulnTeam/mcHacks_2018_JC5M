from flask import Flask, render_template, flash, request, url_for, redirect, session
from forms.sign_in import SignInForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('main_page.html', username=session['username'] if 'username' in session else None)

@app.route('/sign_in/', methods=['GET', 'POST'])
def sign_in():
    sign_in_form = SignInForm(request.form)
    print(request.method)
    if request.method == "POST" and sign_in_form.validate_on_submit():
        print('fdsafa')
        if not db.users.find_one({'username': sign_in_form.username.data}):
            user = User(sign_in_form.email.data, sign_in_form.username.data, sign_in_form.password.data)
            db.users.insert_one(user.json())
            session['username']= user.username
            session['email']= user.email
            return redirect(url_for('index'))
        else:
            flash('username already exists')
            return render_template('sign_in.html', form=sign_in_form)
    return render_template('sign_in.html', form=sign_in_form)
"""
@app.route('/upload_photo', methods = ['GET', 'POST'])
def upload_photo():
    

    app = Flask(__name__)
    client = MongoClient(host='localhost', port=27017)
    db = client.data


    @app.route('/upload_photos/', methods = ["GET", "POST"])
    def upload_photo():
        if request.method == "POST":
            # Get photo from request
            new_photo = request.args.get('upload_file')
            # Save file
            filename = secure_filename(new_photo)
            new_photo.save(os.path.join(app.config['Photos'], filename))


    """



if __name__ == '__main__':
    app.run()
