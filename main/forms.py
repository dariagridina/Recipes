from django import forms

from main.models import Recipe


class SearchForm(forms.Form):
    name = forms.CharField()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image']
