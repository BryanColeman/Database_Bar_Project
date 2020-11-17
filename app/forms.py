from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Optional


class LoginForm(FlaskForm):
    bartender_id = StringField('username', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    bartender_id = StringField('Bartender ID', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    middle_name = StringField('Middle Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    work_monday = BooleanField('Monday 4-11 PM')
    work_tuesday = BooleanField('Tuesday 4-11 PM')
    work_wednesday = BooleanField('Wednesday 4-11 PM')
    work_thursday = BooleanField('Thursday 4-11 PM')
    work_friday = BooleanField('Friday 4-12 PM')
    work_saturday = BooleanField('Saturday 4-12 PM')
    work_sunday = BooleanField('Sunday 4-9 PM')
    wage = IntegerField('Wage', validators=[DataRequired()])
    submit = SubmitField('Register')

    #validate bartender_id