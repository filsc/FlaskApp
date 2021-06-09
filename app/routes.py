from app import app
from flask import render_template, Flask, redirect, url_for, request
from .forms import UserInfoForm

# @app.route('/')
# def index():
#     return render_template('index.html', form=form)



@app.route('/', methods=["POST", ])
def login():
    form= UserInfoForm()
    if request.method == "POST":
        #form_email = request.form['email']
        user = request.form["username"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('index.html', form=form)




    