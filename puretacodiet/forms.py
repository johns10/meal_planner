from django import forms
from django.forms import ModelForm

from puretacodiet.models import *

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'photo', 'info', 'servings', 'directions']
        
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['title', 'photo', 'calories', 'protein', 'fat', 'carbohydrates']

class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['recipe','quantity', 'uom', 'ingredient']

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['title','description', 'dietplan', 'meals']

class DietPlanForm(ModelForm):
    class Meta:
        model = DietPlan
        fields = ['title','description', 'quantity']
        
class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['title']
        
class MealItemForm(ModelForm):
    class Meta:
        model = MealItem
        fields = ['meal', 'recipe']