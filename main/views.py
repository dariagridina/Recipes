from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView

from main.models import Recipe


class RecipeListView(ListView):
    model = Recipe


class RecipeDetailView(DetailView):
    model = Recipe


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return super(CustomLoginView, self).post(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    next_page = '/login'

