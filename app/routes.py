from flask import render_template, url_for, flash
from flask_login import current_user, logout_user, login_user
from werkzeug.utils import redirect

from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import Employee, Drink


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('menu', id=current_user.id))
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(id=form.bartender_id.data).first()
        if employee is None:
            flash('invalid employee ID')
            return redirect(url_for('login'))
        login_user(employee)
        return redirect(url_for('menu'))
    return render_template('login.html', title='sign on', form=form)


@app.route('/stock', methods=['GET', 'POST'])
def stock():
    beerDict = dict
    rumDict = dict
    vodkaDict = dict
    bourbonDict = dict
    ryeDict = dict
    scotchDict = dict
    ginDict = dict
    supply = Drink.query.all()

    for s in supply:
        if s.Type == 'beer':
            beerDict[s.Name] = s.Supply
        if s.Type == 'rum':
            rumDict[s.Name] = s.Supply
        if s.Type == 'vodka':
            vodkaDict[s.Name] = s.Supply
        if s.Type == 'bourbon':
            bourbonDict[s.Name] = s.Supply
        if s.Type == 'rye':
            ryeDict[s.Name] = s.Supply
        if s.Type == 'scotch':
            scotchDict[s.Name] = s.Supply
        if s.Type == 'gin':
            ginDict[s.Name] = s.Supply

    return render_template('stock.html', title='bar stock',
                           beerDict=beerDict, rumDict=rumDict, vodkaDict=vodkaDict,
                           bourbonDict=bourbonDict, ryeDict=ryeDict, scotchDict=scotchDict,
                           ginDict=ginDict)


@app.route('/drink_menu', methods=['GET', 'POST'])
def drink_menu():
    return render_template('drink_menu.html', title='bar drink menu')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html', title='bar selection menu')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('menu'))
    form = RegisterForm()
    if form.validate_on_submit():
        work_days = ""
        if form.work_monday.data:
            work_days = 'monday,'
        if form.work_tuesday.data:
            work_days = 'tuesday,'
        if form.work_wednesday.data:
            work_days = 'wednesday,'
        if form.work_thursday.data:
            work_days = 'thursday,'
        if form.work_friday.data:
            work_days = 'friday,'
        if form.work_saturday.data:
            work_days = 'saturday,'
        if form.work_sunday.data:
            work_days = 'sunday,'
        employee = Employee(id=form.bartender_id.data,
                            Wages=6,
                            Shift=work_days,
                            Name=form.first_name.data + " " + form.middle_name.data + " " + form.last_name.data)
        db.session.add(employee)
        db.session.commit()
        flash('You are now registered!')
        return redirect(url_for('login'))
    return render_template('newuser.html', title='register', form=form)
