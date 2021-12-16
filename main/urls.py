from django.urls import path

from main.views import RecipeDetailView, RecipeListView, FavouritesListView, AddFavouritesView, NewRecipeView

urlpatterns = [
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('favourites/', FavouritesListView.as_view(), name='favourite_recipes'),
    path('favourites/add/<pk>/', AddFavouritesView.as_view(), name='add_to_favourites'),
    path('new/', NewRecipeView.as_view(), name='new_recipe'),
]
