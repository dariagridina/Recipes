from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=4096, null=True, blank=True)
    image = models.ImageField(upload_to='recipe/images/', null=True, blank=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True
    )

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.FloatField(validators=[MinValueValidator(0)])
    unit = models.ForeignKey('main.Unit', on_delete=models.PROTECT)


class Menu(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Instruction(models.Model):
    class Meta:
        ordering = ['order']

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    order = models.IntegerField()
    step = models.TextField(max_length=512)

    def __str__(self):
        return self.step


class Unit(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shopping_list')


class ShoppingListElement(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
