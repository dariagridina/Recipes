from django.urls import path

from main.views import RecipeDetailView, RecipeListView, BaseHtmlOpen

urlpatterns = [
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),
    path('', BaseHtmlOpen.as_view(), name='base')
]
