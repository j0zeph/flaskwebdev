#!/usr/bin/env python3

from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_moment import Moment
import os


# take environment variables from .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret_key')
print(app.config['SECRET_KEY'])

moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name=username)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
