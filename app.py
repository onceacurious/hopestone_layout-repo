from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import Services, Works


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:*#4Kgdngf$KTGM@localhost/hopestone'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    userName = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(15))
    confirm = db.Column(db.String(15))
    email = db.Column(db.String(50))
    contact = db.Column(db.String(15))

    def __init__(self, name, userName, password, email, contact):
        self.name = name
        self.userName = userName
        self.password = password
        self.email = email
        self.contact = contact


Services = Services()
Works = Works()


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/work')
def works():
    return render_template('work.html', works=Works)


@app.route('/services')
def services():
    return render_template('services.html', services=Services)


@app.route('/service/<string:title>/')
def service(title):
    return render_template(
        'service.html',
        title=title
    )


class RegisterFrom(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    userName = StringField('Username', [
        validators.Length(min=3, max=15)
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confrim Password')
    email = StringField('Email Address', [
        validators.Length(min=6, max=50),

    ])
    contact = StringField('Contact', [validators.Length(min=7, max=15)])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterFrom(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('register.html')

    return render_template('register.html', form=form)
