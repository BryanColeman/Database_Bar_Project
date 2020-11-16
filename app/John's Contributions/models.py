#Rough first attempt, check thoroughly before adding to project
from django.db import models

class Drink(models.Model):
    drID = models.CharField(max_length=20)        #Can be set to IntegerField?
    Brand = models.CharField(max_length=250)
    Supply = models.IntegerField                  #???
    Type = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)

class Cocktail(models.Model):
    ckID = models.CharField(max_length=20)      #Can be set to IntegerField?
    Name = models.CharField(max_length=250)
    Ratio = models.                             #unclear how it would work, char field offset by spaces? 20 50 30 = 20% ingred1 50% ingred2 30% ingred3?
    Ingredients = models.ForeignKey(Drink)   #??? Look more into how many -> many relationships work, tutorial suggests using on_delet=models.cascade, but seems to only be essential for one -> many

class Menu_Item(models.Model):
    mID = models.CharField(max_length=20)       #Can be set to IntegerField?
    Price = models.DecimalField()               #???
    Amount_Used = models.IntegerField()         #???

class Employee(models.Model):
    empID = models.CharField(max_length=20)     #Can be set to IntegerField?
    Wages = models.DecimalField()   #???
    Shift = models.DateTimeField()   #???
    Name = models.CharField(max_length=250)
