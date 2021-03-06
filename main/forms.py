from django import forms
from django.forms import inlineformset_factory

from main.models import Recipe, IngredientInRecipe, Instruction


class SearchForm(forms.Form):
    name = forms.CharField()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].label = 'Upload Image'


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
        self.fields['step'].label = False


IngredientInRecipeFormSet = inlineformset_factory(model=IngredientInRecipe, parent_model=Recipe, form=IngredientInRecipeForm,
                                                  extra=0, min_num=1, validate_min=True, can_delete_extra=False)
InstructionFormSet = inlineformset_factory(model=Instruction, parent_model=Recipe, form=InstructionForm,
                                           extra=0, min_num=1, validate_min=True, can_delete_extra=False)
