from django.contrib import admin
from . import models
# Register your models here.


class FlavorInline(admin.StackedInline):
    model = models.Flavor


class FlavorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(models.Flavor, FlavorAdmin)


class MealAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(models.Meal, MealAdmin)


class UnitAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(models.Unit, UnitAdmin)


class FoodGroupMembershipInline(admin.TabularInline):
    model = models.FoodGroup.ingredients.through


class IngredientAdmin(admin.ModelAdmin):  # TODO make more usable
    search_fields = ['name']
    list_display = ['name']
    inlines = [FoodGroupMembershipInline]


admin.site.register(models.Ingredient, IngredientAdmin)


class FoodGroupAdmin(admin.ModelAdmin):  # TODO make more usable
    search_fields = ['name']
    list_display = ['name']
    inlines = [FoodGroupMembershipInline]
    exclude = ['members']


admin.site.register(models.FoodGroup, FoodGroupAdmin)


class DietAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']


admin.site.register(models.Diet, DietAdmin)


class RecipeAdmin(admin.ModelAdmin):  # TODO make more usable
    search_fields = ['title']
    list_display = ['title']


admin.site.register(models.Recipe, RecipeAdmin)

# TODO added recipeingredients admin
