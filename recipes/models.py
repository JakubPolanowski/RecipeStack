from django.db import models

# Create your models here.


class Flavor(models.Model):
    # various flavors that are attached to recipes many to many
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    # various meals (such as morning, Dinner) that are attached to recipes many to many
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    # volume, temperature, etc. units
    name = models.CharField(max_length=50, unique=True)
    shorthand = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class UnitConversion(models.Model):
    from_unit = models.ForeignKey(
        Unit, related_name='from_unit', on_delete=models.CASCADE)
    factor = models.FloatField()
    to_unit = models.ForeignKey(
        Unit, related_name='to_unit', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.from_unit} to {self.to_unit}"


class Ingredient(models.Model):
    # ingredient used in recipe
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class FoodGroup(models.Model):
    # food groups that ingredients belong in
    name = models.CharField(max_length=50, unique=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name


class Diet(models.Model):
    # diet that are attached to recipes many to many
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    flavors = models.ManyToManyField(Flavor)
    meals = models.ManyToManyField(Meal)
    diets = models.ManyToManyField(Diet)
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredients')

    # TODO figure out how to handle steps/instructions

    def __str__(self):
        return self.title


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    amount = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
