from django.shortcuts import render, get_object_or_404
from main.models import Recipe


def get_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'main/recipe.html', context)
