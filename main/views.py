from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from main.models import Recipe


class RecipeListView(ListView):
    model = Recipe

    def get_context_data(self, **kwargs):
        kwargs['favourite_recipes'] = Recipe.objects.filter(favourites=self.request.user)
        return super(RecipeListView, self).get_context_data(**kwargs)


class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        is_favourite = False
        if self.object.favourites.filter(id=self.request.user.id).exists():
            is_favourite = True
        kwargs['is_favourite'] = is_favourite
        return super(RecipeDetailView, self).get_context_data(**kwargs)


class FavouritesListView(ListView):
    model = Recipe
    template_name = 'main/favourite_recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(favourites=self.request.user)


class AddFavouritesView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

