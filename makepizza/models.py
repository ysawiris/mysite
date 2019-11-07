from django.db import models

# Create your models here.
class Topping(models.Model):
    cheese = models.CharField(max_length=100)
    meat = models.CharField(max_length=100)
    sauce = models.CharField(max_length=100)


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)