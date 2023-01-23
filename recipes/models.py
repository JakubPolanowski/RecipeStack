from django.db import models

# Create your models here.


class Flavor(models.Model):
    # various flavors that are attached to recipes many to many
    name = models.CharField(max_length=50)


class Meal(models.Model):
    # various meals (such as morning, Dinner) that are attached to recipes many to many
    name = models.CharField(max_length=50)


class Unit(models.Model):  # TODO figure out how to handle compatible units/conversion
    # volume, temperature, etc. units
    name = models.CharField(max_length=10)


class Ingredient(models.Model):
    # ingredient used in recipe
    name = models.CharField(max_length=50)


class FoodGroup(models.Model):
    # food groups that ingredients belong in
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)


class Diet(models.Model):
    # diet that are attached to recipes many to many
    name = models.CharField(max_length=50)


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    flavors = models.ManyToManyField(Flavor)
    meals = models.ManyToManyField(Meal)
    diets = models.ManyToManyField(Diet)
    # TODO figure out how to handle steps/instructions


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    amount = models.FloatField()
