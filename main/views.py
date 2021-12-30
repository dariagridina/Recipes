from django.http import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

from main.forms import SearchForm, RecipeForm, IngredientInRecipeFormSet, IngredientInRecipeForm, InstructionFormSet
from main.models import Recipe


class RecipeListView(ListView):
    model = Recipe

    def get_context_data(self, **kwargs):
        kwargs['favourite_recipes'] = Recipe.objects.filter(favourites=self.request.user)
        kwargs['hide_header_search'] = True
        return super(RecipeListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        queryset = super(RecipeListView, self).get_queryset()
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            queryset = queryset.filter(name__contains=name)
        return queryset


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

    def get_context_data(self, **kwargs):
        kwargs['hide_header_search'] = True
        return super(FavouritesListView, self).get_context_data(**kwargs)


class AddFavouritesView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class NewRecipeView(CreateView):
    model = Recipe
    template_name = 'main/new_recipe.html'
    form_class = RecipeForm

    def get_context_data(self, **kwargs):
        if self.request.POST:
            kwargs['ingredient_formset'] = IngredientInRecipeFormSet(self.request.POST, prefix='ingredients')
            kwargs['step_formset'] = InstructionFormSet(self.request.POST, prefix='steps')
        else:
            kwargs['ingredient_formset'] = IngredientInRecipeFormSet(prefix='ingredients')
            kwargs['step_formset'] = InstructionFormSet(prefix='steps')
        return super(NewRecipeView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        recipe_form = self.get_form()
        ingredient_formset = IngredientInRecipeFormSet(request.POST, prefix='ingredients')
        instruction_formset = InstructionFormSet(request.POST, prefix='steps')

        if recipe_form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
            self.object = recipe_form.save()
            for form in ingredient_formset:
                ingredient = form.save(commit=False)
                ingredient.recipe = self.object
                ingredient.save()

            for order, form in enumerate(instruction_formset):
                instruction = form.save(commit=False)
                instruction.recipe = self.object
                instruction.order = order
                if instruction.step:
                    instruction.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            return self.render_to_response(self.get_context_data(form=recipe_form))
