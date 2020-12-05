from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Optional, ValidationError

from app.models import Employee


class DeleteForm(FlaskForm):
    bartender_id = StringField('Bartender ID', validators=[DataRequired()])
    submit = SubmitField('Delete')


class LoginForm(FlaskForm):
    bartender_id = StringField('Bartender ID', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    bartender_id = IntegerField('Bartender ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    work_monday = BooleanField('Mon 4-11 PM')
    work_tuesday = BooleanField('Tue 4-11 PM')
    work_wednesday = BooleanField('Wed 4-11 PM')
    work_thursday = BooleanField('Thu 4-11 PM')
    work_friday = BooleanField('Fri 4-12 PM')
    work_saturday = BooleanField('Sat 4-12 PM')
    work_sunday = BooleanField('Sun 4-9 PM')
    submit = SubmitField('Register')


class DrinkButtonForm(FlaskForm):
    budlight_bottle = SubmitField('Bud Light')
    yuengling_bottle = SubmitField('Yuengling')
    budweiser_bottle = SubmitField('Budweiser')
    guinness_bottle = SubmitField('Guinness')
    dos_equis_bottle = SubmitField('Dos Equis')
    shiner_bock_bottle = SubmitField('Shiner Bock')
    lagavulin_16_neat = SubmitField('Lagavulin 16 Neat')
    old_fashioned = SubmitField('Old Fashioned')
    manhattan = SubmitField('Manhattan')
    martini = SubmitField('Martini')
    daiquiri = SubmitField('Daiquiri')
    black_russian = SubmitField('Black Russian')
    finished = SubmitField('Back')
