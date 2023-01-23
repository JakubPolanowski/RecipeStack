from django.db import models

# Create your models here.


class Flavor(models.Model):
    # various flavors that are attached to recipes many to many
    name = models.CharField(max_length=50)


class Meal(models.Model):
    # various meals (such as morning, Dinner) that are attached to recipes many to many
    name = models.CharField(max_length=50)


class Ingredient(models.Model):
    # ingredient used in recipe
    name = models.CharField(max_length=50)


class FoodGroups(models.Model):
    # food groups that ingredients belong in
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)


class Diets(models.Model):
    # diet that are attached to recipes many to many
    name = models.CharField(max_length=50)


# TODO Recipe
# title
# content
# flavor
# meal
# ingredients
# diets
