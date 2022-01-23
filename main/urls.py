from django.urls import path

from main.views import RecipeDetailView, RecipeListView, FavouritesListView, FavouritesAddView, NewRecipeView, \
    ShoppingListView, AddRecipeToShoppingListView, ShoppingListElementView, EditRecipeUpdateView, MyRecipesAddView, \
    MyRecipesListView, MyRecipeDeleteView

urlpatterns = [
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<pk>/edit', EditRecipeUpdateView.as_view(), name='edit_page'),
    path('recipe/<pk>/delete', MyRecipeDeleteView.as_view(), name='delete_my_recipe'),
    path('recipes/', RecipeListView.as_view(), name='recipe_list'),
    path('my_recipes/', MyRecipesListView.as_view(), name='my_recipes'),
    path('my_recipes/add/<pk>', MyRecipesAddView.as_view(), name='add_to_my_recipes'),
    path('favourites/', FavouritesListView.as_view(), name='favourite_recipes'),
    path('favourites/add/<pk>/', FavouritesAddView.as_view(), name='add_to_favourites'),
    path('new/', NewRecipeView.as_view(), name='new_recipe'),
    path('shopping_list/', ShoppingListView.as_view(), name='shopping_list'),
    path('shopping_list/add/<pk>/', AddRecipeToShoppingListView.as_view(), name='add_to_shopping_list'),
    path('shopping_list/element/', ShoppingListElementView.as_view(), name='shopping_list_element_list'),
    path('shopping_list/element/<pk>/', ShoppingListElementView.as_view(), name='shopping_list_element_detail'),
]
