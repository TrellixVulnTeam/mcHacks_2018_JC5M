from flask import Flask, render_template, flash, request, url_for, redirect, session

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    #return render_template('main_page.html', username=session['username'] if 'username' in session else None)

@app.route('/voting/', methods = ['GET','POST'])
def voter():
    """
    error = ''
    try:
        if request.method== "POST":fdsafdasds
            attempted_username = request.form['username']
            attempted_password= request.form['psw']
            attempted_email = request.form['email']
#   
            flash(attempted_username)
            flash(attempted_p##assword)

            if  db.users.find_one({u'username':"{}".format(attempted_username),u'password':attempted_password}):
                flash("found")
                session['username'] = attempted_username
                session['email'] = attempted_email
                return redirect(url_for('index'))
            else:
                error = "Not Valid Credentials. Try again."

        return render_template("l#####fdsafdaogin.html", error = error)

    except Exception as e:
        flash(e)
        return render_template("login.html", error= error)

"""
    return render_template('main_page.html')



if __name__ == '__main__':
    app.run()
