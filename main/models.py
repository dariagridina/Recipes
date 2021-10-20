from django.db import models
from django.core.validators import MinValueValidator


class Ingredient(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4096, null=True, blank=True)

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    unit = models.ForeignKey('main.Unit', on_delete=models.PROTECT)


class Menu(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name