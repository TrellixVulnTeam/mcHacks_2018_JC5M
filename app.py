import pymongo
from flask import Flask, render_template, flash, request, url_for, redirect, session
from forms.sign_in import SignInForm
from database import Database
from models.user import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


app.config.from_object('config')


db= Database().db
#app.config mongo
###########3
#mongo=pymongo(app)##

#print(db.collection_names())





#client = MongoClient("mongodb://<dbuser>:<dbpassword>@ds123698.mlab.com:23698/dbdatabase")
#db = client['dbdatabase']
#user_records=db.user_records



##


#
@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('main_page.html', username=session['username'] if 'username' in session else None)



@app.route('/view_results/', methods = ['GET','POST'])
def view_results():

    all_requests = db.users.find_one({"username":"nba"})
    print(all_requests['images'])
    return render_template('view_results.html', username = session['username'] if 'username' in session else None, requests=all_requests)


im=['fdsfads','fdsafdsa','fsdafdas']

@app.route('/sign_in/', methods=['GET', 'POST'])
#SIGN-UP
def sign_in():
    sign_in_form = SignInForm(request.form)
    print(request.method)
    if request.method == "POST":
        #if request.method == "POST" and sign_in_form.validate_on_submit():
        print('fdsafa')
        if not db.users.find_one({'username': sign_in_form.username.data}):
            user = User(sign_in_form.email.data, sign_in_form.username.data, sign_in_form.password.data)
            print(user.username)
            db.users.insert_one(user.json())
            session['username']= user.username
            session['email']= user.email
            return render_template('view_results.html')
            #return redirect(url_for('index'))

        else:
            flash('username already exists')
            return render_template('sign_in.html', form=sign_in_form)
    return render_template('sign_in.html', form=sign_in_form)

@app.route('/login/', methods = ['GET','POST'])
def login_page():
    error = ''
    try:
        if request.method== "POST":
            print('fdsafdsafsdsda')
            attempted_username = request.form['username']
            attempted_password= request.form['psw']
            #attempted_email = request.form['email']

            flash(attempted_username)
            flash(attempted_password)
#

            if  db.users.find_one({u'username':"{}".format(attempted_username),u'password':attempted_password}):
                flash("found")
                session['username'] = attempted_username
                session['email'] = attempted_email
                return redirect(url_for('view_results'))
            else:
                error = "Not Valid Credentials. Try again."

        return render_template("login.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error= error)

    return render_template('login.html')

@app.route('/upload_photo/', methods = ['GET', 'POST'])
def upload_photo():
    """
    def upload_photo():
        if request.method == "POST":
            # Get photo from request
            new_photo = request.args.get('upload_file')
            # Save file
            filename = secure_filename(new_photo)
            new_photo.save(os.path.join(app.config['Photos'], filename))
    """
    return render_template('upload_photo.html')

if __name__ == '__main__':
    app.run()

