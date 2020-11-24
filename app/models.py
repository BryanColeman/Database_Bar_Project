from app import login
from flask import Flask
from flask_sqlalchemy import sqlalchemy

class Drink(db.Model):
     drID = db.Column(db.Integer, primary_key = True)
     Brand = db.Column(db.String(250), nullable=False) 
     Supply = db.Column(db.Integer, nullable=False)
     Type = db.Column(db.String(250), nullable=False)
     Name = db.Column(db.String(250), unique=True, nullable=False)

class Cocktail(db.Model):
     ckID = db.Column(db.Integer, primary_key = True)
     Name = db.Column(db.String(250), unique=True, nullable=False)
     Ratio = db.Column                      #???
     Ingredients = db.relationship('Drink', backref='Cocktail', lazy=True)

class Menu_Item(db.Model):

     mID = db.Column(db.Integer, primary_key = True)
     Price = db.Column(db.Integer, nullable=False)
     Amount_Used = db.Column(db.Integer, nulable=False)

class Employee(db.Model):
     empID = db.Column(db.Integer, primary_key = True)
     Wages = db.Column(db.Integer, nullable=False)
     Shift = db.Column(db.DateTime, nullable=False)
     Name = db.Column(db.String(250), unique=True, nullable=False)

@login.user_loader
def load_user(id):
    print('temp')
    #query db to load user