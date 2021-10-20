from django.contrib import admin
from main.models import Ingredient, Recipe, IngredientInRecipe, Menu, Unit


class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientInRecipe


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInRecipeInline
    ]


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Menu)
admin.site.register(Unit)