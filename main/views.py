from django.views.generic import ListView, DetailView, TemplateView

from main.models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe
