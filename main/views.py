from django.shortcuts import render, get_object_or_404, HttpResponse
from main.models import Recipe


def list_of_recipes(request):
    all_recipes = Recipe.objects.all()
    context = {
        'all_recipes': all_recipes,
    }
    return render(request, 'main/recipe.html', context)



def get_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'main/recipe_bootstrap.html', context)
