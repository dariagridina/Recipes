from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class CustomLoginView(LoginView):
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = '/login'


class RegistrationView(CreateView):
    template_name = 'registration/sign_up.html'
    model = User
    form_class = UserCreationForm
    success_url = '/recipe'
