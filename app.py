from flask import Flask, render_template, request, redirect
from forms import registration_form
from flask_sqlalchemy import SQLAlchemy
from model import db, User
from flask_wtf.csrf import CsrfProtect
import os
SECRET_KEY = os.urandom(32)

app = Flask(__name__)
database = SQLAlchemy(app)
database.create_all()
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/index')
def hello_world():
    return render_template("index.html")


@app.route('/register')
def register():
    form = registration_form()
    if request.method == "POST":
        form = registration_form(request.form)
        if form.validate_on_submit():
            user = User(None, form.email, form.username, form.password)
            database.session.add(user)
            database.session.commit()
        return redirect("/index")
    return render_template("register.html", form=form)



if __name__ == '__main__':
    app.run()
