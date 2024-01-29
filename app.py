from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = '55697b00b4c994fd77efb4355c7bb7b6a8c1bfa9b636f3b3'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')


if __name__ == '__main__':
    app.run()
