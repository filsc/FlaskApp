from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

# @app.route('/')
# @app.route('/index')
# def hello_world():
#     return render_template('index.html')

# @app.route('/login', methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template('index.html')


# from flask_login import LoginManager