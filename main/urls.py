from django.urls import path

from main.views import RecipeDetailView, RecipeListView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('recipe/<pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/', RecipeListView.as_view(), name='recipe_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
