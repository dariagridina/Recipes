import re

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.forms import SearchForm, RecipeForm, IngredientInRecipeFormSet, InstructionFormSet
from main.models import Recipe, IngredientInRecipe, ShoppingListElement, ShoppingList, Ingredient, Unit


class RecipeListView(ListView):
    model = Recipe

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            kwargs['favourite_recipes'] = Recipe.objects.filter(favourites=self.request.user)
        kwargs['hide_header_search'] = True
        return super(RecipeListView, self).get_context_data(**kwargs)

    def get_queryset(self):
        queryset = super(RecipeListView, self).get_queryset()
        queryset = queryset.filter(user=None)
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            queryset = queryset.filter(name__contains=name)
        return queryset


class RecipeDetailView(DetailView):
    model = Recipe

    def get_queryset(self):
        queryset = super(RecipeDetailView, self).get_queryset()
        queryset = queryset.filter(Q(user=self.request.user) | Q(user=None))
        return queryset

    def get_context_data(self, **kwargs):
        is_favourite = False
        if self.object.favourites.filter(id=self.request.user.id).exists():
            is_favourite = True
        kwargs['is_favourite'] = is_favourite
        return super(RecipeDetailView, self).get_context_data(**kwargs)


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
            self.object.user = request.user
            self.object.save()
            for form in ingredient_formset:
                if form.cleaned_data:
                    ingredient = form.save(commit=False)
                    ingredient.recipe = self.object
                    ingredient.save()
            for order, form in enumerate(instruction_formset):
                if form.cleaned_data:
                    instruction = form.save(commit=False)
                    instruction.recipe = self.object
                    instruction.order = order
                    instruction.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            return self.render_to_response(self.get_context_data(form=recipe_form))


class EditRecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'main/edit_page.html'
    form_class = RecipeForm

    def get_context_data(self, **kwargs):

        if self.request.POST:
            kwargs['ingredient_formset'] = IngredientInRecipeFormSet(self.request.POST,
                                                                     prefix='ingredients', instance=self.object)
            kwargs['step_formset'] = InstructionFormSet(self.request.POST, prefix='steps', instance=self.object)
        else:
            kwargs['ingredient_formset'] = IngredientInRecipeFormSet(prefix='ingredients', instance=self.object)
            kwargs['step_formset'] = InstructionFormSet(prefix='steps', instance=self.object)
        return super(EditRecipeUpdateView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        recipe_form = self.get_form()
        ingredient_formset = IngredientInRecipeFormSet(request.POST, prefix='ingredients', instance=self.object)
        instruction_formset = InstructionFormSet(request.POST, prefix='steps', instance=self.object)

        if recipe_form.is_valid() and ingredient_formset.is_valid() and instruction_formset.is_valid():
            self.object = recipe_form.save()
            self.object.user = request.user
            self.object.save()
            for form in ingredient_formset:
                if form.changed_data == ['DELETE']:
                    form.instance.delete()
                    continue
                if form.cleaned_data:
                    ingredient = form.save(commit=False)
                    ingredient.recipe = self.object
                    ingredient.save()
            for order, form in enumerate(instruction_formset):
                if form.changed_data == ['DELETE']:
                    form.instance.delete()
                    continue
                if form.cleaned_data:
                    instruction = form.save(commit=False)
                    instruction.recipe = self.object
                    instruction.order = order
                    instruction.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            self.object = None
            return self.render_to_response(self.get_context_data(form=recipe_form))


class FavouritesListView(ListView):
    model = Recipe
    template_name = 'main/favourite_recipes.html'

    def get_queryset(self):
        queryset = super(FavouritesListView, self).get_queryset()
        queryset = queryset.filter(favourites=self.request.user)
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            queryset = queryset.filter(name__contains=name)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['hide_header_search'] = True
        kwargs['favourite_recipes'] = Recipe.objects.filter(favourites=self.request.user)
        return super(FavouritesListView, self).get_context_data(**kwargs)


class FavouritesAddView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        if recipe.favourites.filter(id=request.user.id).exists():
            recipe.favourites.remove(request.user)
        else:
            recipe.favourites.add(request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class MyRecipesListView(ListView):
    model = Recipe
    template_name = 'main/my_recipes.html'

    def get_queryset(self):
        queryset = super(MyRecipesListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        form = SearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data['name']
            queryset = queryset.filter(name__contains=name)
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['hide_header_search'] = True
        kwargs['favourite_recipes'] = Recipe.objects.filter(favourites=self.request.user)
        return super(MyRecipesListView, self).get_context_data(**kwargs)


class MyRecipesAddView(View):

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.id = None
        recipe.user = request.user
        recipe.save()

        old_recipe = Recipe.objects.get(pk=pk)
        for ing in old_recipe.ingredientinrecipe_set.all():
            ing.id = None
            ing.recipe = recipe
            ing.save()

        for step in old_recipe.instruction_set.all():
            step.id = None
            step.recipe = recipe
            step.save()
        return HttpResponseRedirect(reverse('recipe_detail', kwargs={'pk': recipe.id}))


class MyRecipeDeleteView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
        recipe.delete()
        return HttpResponseRedirect(reverse('my_recipes'))


class ShoppingListView(ListView):
    model = IngredientInRecipe
    template_name = 'main/shopping_list.html'

    def get_context_data(self, **kwargs):
        kwargs['shopping_list'] = self.request.user.shopping_list
        return super(ShoppingListView, self).get_context_data(**kwargs)


class AddRecipeToShoppingListView(View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)

        for i in recipe.ingredientinrecipe_set.all():
            element, created = ShoppingListElement.objects.get_or_create(shopping_list=request.user.shopping_list,
                                                                         ingredient=i.ingredient, unit=i.unit,
                                                                         completed=False,
                                                                         defaults={'quantity': i.quantity})
            if not created:
                element.quantity += i.quantity
                element.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


class ShoppingListElementView(View):
    def put(self, request, pk):
        element = get_object_or_404(ShoppingListElement, pk=pk, shopping_list__user=request.user)
        element.completed = not element.completed
        element.save()
        return HttpResponse(status=200)

    def delete(self, request, pk):
        element = get_object_or_404(ShoppingListElement, pk=pk, shopping_list__user=request.user)
        element.delete()
        return HttpResponse(status=200)

    def post(self, request):
        user_input = request.POST['input']
        regex = (r'((?P<name>[a-zA-Z\ ]+?)\s?(?P<quantity>\d+\.?,?\d*)\s?(?P<unit>[a-zA-Z]*\s*?|$)|'
                 r'(?P<quantity2>\d+\.?,?\d*)\s?(?P<unit2>[a-zA-Z]*)(\ +?|$)(?P<name2>[a-zA-Z\ ]+)?)')
        compiled = re.compile(regex)
        match = compiled.search(user_input)
        if match:
            name = match.group('name') or match.group('name2')
            quantity = float(match.group('quantity') or match.group('quantity2'))
            unit_name = match.group('unit') or match.group('unit2')
        else:
            name = user_input
            quantity = 1
            unit_name = 'item'

        ingredient, _ = Ingredient.objects.get_or_create(name__iexact=name, defaults={
            'name': name.lower()
        })
        unit, _ = Unit.objects.get_or_create(name__iexact=unit_name, defaults={
            'name': unit_name.lower()
        })

        element, created = ShoppingListElement.objects.get_or_create(shopping_list=request.user.shopping_list,
                                                                     ingredient=ingredient, unit=unit, completed=False,
                                                                     defaults={'quantity': quantity})
        if not created:
            element.quantity += quantity
            element.save()
        return JsonResponse(status=200, data={'unit_name': element.unit.name, 'quantity': element.quantity,
                                              'ingredient_name': element.ingredient.name})
