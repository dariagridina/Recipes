from django.contrib.auth import views
from django.urls import path

from accounts.views import CustomLoginView, RegistrationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', RegistrationView.as_view(), name='sign_up'),
]
