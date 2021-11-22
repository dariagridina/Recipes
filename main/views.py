from django.views.generic import ListView, DetailView

from main.models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe


class FavouritesListView(ListView):
    model = Recipe
    template_name = 'main/favourite_recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(favourites__in=[self.request.user])
