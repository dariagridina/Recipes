from django.shortcuts import render
from main.models import Recipe


def get_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        'recipe': recipe
    }
    return render(request, 'main/recipe.html', context)
