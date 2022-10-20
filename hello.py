#!/usr/bin/env python3

from dotenv import load_dotenv

from flask import Flask, render_template

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os


# take environment variables from .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('secret_key')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()

    # if the form was submitted
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = '' # reset the form field
    
    return render_template('index.html', form=form, name=name)


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name=username)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Form classes
class NameForm(FlaskForm):
    name = StringField(label='What is your name?', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


if __name__ == '__main__':
    app.run(debug=True)
