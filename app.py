from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/work')
def work_page():
    return render_template('work.html')


@app.route('/services')
def services_page():
    return render_template('services.html')
