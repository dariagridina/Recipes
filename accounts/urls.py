from django.contrib.auth import views
from django.urls import path

from accounts.views import CustomLoginView, CustomLogoutView, RegistrationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', RegistrationView.as_view(), name='sign_up'),
]
