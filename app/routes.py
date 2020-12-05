from flask import render_template, url_for, flash, request
from flask_login import current_user, logout_user, login_user
from werkzeug.utils import redirect

from app import app, db
from app.forms import LoginForm, RegisterForm, DrinkButtonForm, DeleteForm
from app.models import Employee, Drink, Cocktail


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

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        Employee.query.filter_by(id=form.bartender_id.data).delete()
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html', form=form)


@app.route('/stock', methods=['GET', 'POST'])
def stock():
    beerDict = {}
    rumDict = {}
    vodkaDict = {}
    bourbonDict = {}
    ryeDict = {}
    scotchDict = {}
    ginDict = {}
    supply = Drink.query.all()

    totalbeersupply = 0
    for s in supply:
        print(s.Name)
        if s.Name == 'BudLight':
            beerDict[s.Name] = s.Supply
            totalbeersupply = totalbeersupply + s.Supply
        if s.Name == 'Yuengling':
            beerDict[s.Name] = s.Supply
            totalbeersupply = totalbeersupply + s.Supply
        if s.Name == 'Budweiser':
            beerDict[s.Name] = s.Supply
            totalbeersupply = totalbeersupply + s.Supply
        if s.Name == 'Guinness':
            beerDict[s.Name] = s.Supply
            totalbeersupply = totalbeersupply + s.Supply
        if s.Name == 'Dos Equis':
            beerDict[s.Name] = s.Supply
            totalbeersupply = totalbeersupply + s.Supply
        if s.Name == 'Shiner Bock':
            beerDict[s.Name] = s.Supply
            totalbeersupply = totalbeersupply + s.Supply
        if s.Name == 'Havana Club':
            rumDict[s.Name] = s.Supply
        if s.Name == 'Titos':
            vodkaDict[s.Name] = s.Supply
        if s.Name == 'Woodford Reserve':
            bourbonDict[s.Name] = s.Supply
        if s.Name == 'Mitchers Rye':
            ryeDict[s.Name] = s.Supply
        if s.Name == 'Laugavulin 16':
            scotchDict[s.Name] = s.Supply
        if s.Name == 'Bombay Sapphire':
            ginDict[s.Name] = s.Supply
        print(beerDict)

    return render_template('stock.html', title='bar stock',
                           beerDict=beerDict, rumDict=rumDict, vodkaDict=vodkaDict,
                           bourbonDict=bourbonDict, ryeDict=ryeDict, scotchDict=scotchDict,
                           ginDict=ginDict, totalbeersupply=totalbeersupply)


@app.route('/drink_menu', methods=['GET', 'POST'])
def drink_menu():
    form = DrinkButtonForm()
    if request.method == 'POST':
        if form.budlight_bottle.data:
            drink = Drink.query.filter_by(drID=1).first()
            cocktail = Cocktail.query.filter_by(ckID=1).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.yuengling_bottle.data:
            drink = Drink.query.filter_by(drID=2).first()
            cocktail = Cocktail.query.filter_by(ckID=2).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.budweiser_bottle.data:
            drink = Drink.query.filter_by(drID=3).first()
            cocktail = Cocktail.query.filter_by(ckID=3).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.guinness_bottle.data:
            drink = Drink.query.filter_by(drID=4).first()
            cocktail = Cocktail.query.filter_by(ckID=4).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.dos_equis_bottle.data:
            drink = Drink.query.filter_by(drID=5).first()
            cocktail = Cocktail.query.filter_by(ckID=5).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.shiner_bock_bottle.data:
            drink = Drink.query.filter_by(drID=6).first()
            cocktail = Cocktail.query.filter_by(ckID=6).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.lagavulin_16_neat.data:
            drink = Drink.query.filter_by(drID=7).first()
            cocktail = Cocktail.query.filter_by(ckID=7).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.old_fashioned.data:
            drink = Drink.query.filter_by(drID=8).first()
            cocktail = Cocktail.query.filter_by(ckID=8).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.manhattan.data:
            drink = Drink.query.filter_by(drID=9).first()
            cocktail = Cocktail.query.filter_by(ckID=9).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.martini.data:
            drink = Drink.query.filter_by(drID=10).first()
            cocktail = Cocktail.query.filter_by(ckID=10).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.daiquiri.data:
            drink = Drink.query.filter_by(drID=11).first()
            cocktail = Cocktail.query.filter_by(ckID=11).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.black_russian.data:
            drink = Drink.query.filter_by(drID=12).first()
            cocktail = Cocktail.query.filter_by(ckID=12).first()
            if drink.Supply <= 0:
                flash(f'There is not a big enough supply of {drink.Name}')
            else:
                ratio = cocktail.Ratio.split(',')
                drink.Supply -= int(ratio[0])
                db.session.commit()
                flash(f'One {cocktail.Name} served')

        if form.finished.data:
            return redirect(url_for('menu'))

    return render_template('drink_menu.html', title='bar drink menu', form=form)


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
