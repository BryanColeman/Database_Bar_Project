from flask_login import UserMixin

from app import login, db
from flask import Flask
from flask_sqlalchemy import sqlalchemy


class Drink(UserMixin, db.Model):
    drID = db.Column(db.Integer, primary_key=True)
    Brand = db.Column(db.String(250), nullable=False)
    Supply = db.Column(db.Integer, nullable=False)
    Type = db.Column(db.String(250), nullable=False)
    Name = db.Column(db.String(250), unique=True, nullable=True)


class Cocktail(UserMixin, db.Model):
    ckID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(250), unique=True, nullable=False)
    Ratio = db.Column(db.String(250), nullable=False)
    Ingredients = db.Column(db.String(250), nullable=False)


class MenuItem(UserMixin, db.Model):
    mID = db.Column(db.Integer, primary_key=True)
    Price = db.Column(db.Integer, nullable=False)
    Amount_Used = db.Column(db.Integer, nullable=True)


class Employee(UserMixin, db.Model):
    empID = db.Column(db.Integer, primary_key=True)
    Wages = db.Column(db.Integer, nullable=False)
    Shift = db.Column(db.String(250), nullable=False)
    Name = db.Column(db.String(250), unique=True, nullable=False)


@login.user_loader
def load_user(id):
    return Employee.query.get(int(empid))
