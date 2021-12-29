from django import forms
from django.forms import formset_factory

from main.models import Recipe, IngredientInRecipe, Instruction


class SearchForm(forms.Form):
    name = forms.CharField()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image']


class IngredientInRecipeForm(forms.ModelForm):
    class Meta:
        model = IngredientInRecipe
        fields = ['ingredient', 'quantity', 'unit']

    def __init__(self, *args, **kwargs):
        super(IngredientInRecipeForm, self).__init__(*args, **kwargs)
        self.fields['ingredient'].widget.attrs.update({'class': 'form-select'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-select'})


class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['step']

    def __init__(self, *args, **kwargs):
        super(InstructionForm, self).__init__(*args, **kwargs)
        self.fields['step'].widget.attrs.update({'class': 'form-control'})


IngredientInRecipeFormSet = formset_factory(IngredientInRecipeForm, extra=0, min_num=1, validate_min=True)
InstructionFormSet = formset_factory(InstructionForm, extra=0, min_num=1, validate_min=True)
