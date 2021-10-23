from django.contrib import admin
from main.models import Ingredient, Recipe, IngredientInRecipe, Menu, Unit, Instruction


class IngredientInRecipeInline(admin.TabularInline):
    model = IngredientInRecipe


class InstructionInline(admin.TabularInline):
    model = Instruction


class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientInRecipeInline,
        InstructionInline,
    ]


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Menu)
admin.site.register(Unit)
