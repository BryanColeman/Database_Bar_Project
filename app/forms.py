from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Optional


class LoginForm(FlaskForm):
    bartender_id = StringField('Bartender ID', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    bartender_id = StringField('Bartender ID', validators=[DataRequired()])
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
    wage = IntegerField('Wage', validators=[DataRequired()])
    submit = SubmitField('Register')

    #validate bartender_id