from flask import render_template, url_for
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from app import app
from app.forms import LoginForm, RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('portal', username=current_user.username))
    form = LoginForm()
    if form.validate_on_submit():
        print("temp")
        # query db for user
        # if user is None:
        # flash invalid redirect to login or index
    # login_user(user,true)
    # return redirect(url_for('portal', username=current_user.username))
    return render_template('login.html', title='sign on', form=form)


@app.route('/stock', methods=['GET', 'POST'])
def stock():
    #query the db to load data to web page
    return render_template('stock.html', title='bar stock')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html', title='bar menu')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('patientportal'))
    form = RegisterForm()
    #add user to db
    if form.validate_on_submit():
        print('temp')
    return render_template('newuser.html', title='register', form=form)