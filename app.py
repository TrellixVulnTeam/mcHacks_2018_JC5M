from flask import Flask, render_template, flash, request, url_for, redirect, session
from forms.sign_in import SignInForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('main_page.html', username=session['username'] if 'username' in session else None)

@app.route('/sign_in/', methods=['GET', 'POST'])
#SIGN-UP
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

@app.route('/login/', methods = ['GET','POST'])
def login_page():
    error = ''
    try:
        if request.method== "POST":
            attempted_username = request.form['username']
            attempted_password= request.form['psw']
            attempted_email = request.form['email']

            flash(attempted_username)
            flash(attempted_password)

            if  db.users.find_one({u'username':"{}".format(attempted_username),u'password':attempted_password}):
                flash("found")
                session['username'] = attempted_username
                session['email'] = attempted_email
                return redirect(url_for('index'))
            else:
                error = "Not Valid Credentials. Try again."

        return render_template("login.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error= error)

    return render_template('login.html')

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
