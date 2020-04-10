from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from puretacodiet.models import *

from puretacodiet.forms import *

from django.urls import reverse

from django.template import loader

def index(request):
    return HttpResponse("Welcome to the Pure Taco Diet")
    
#Recipes    
    
class RecipeListView(ListView):
    model = Recipe
    
class RecipeCreate(CreateView):
    model = Recipe
    form_class = RecipeForm
        
class RecipeDetailView(DetailView):
    model = Recipe

class RecipeUpdate(UpdateView):
    model = Recipe
    form_class = RecipeForm   
    
class RecipeDelete(DeleteView):
    model = Recipe
    
    def get_success_url(self):
        return reverse('puretacodiet:recipes')
    
#Ingredients
    
class IngredientListView(ListView):
    model = Ingredient
    
class IngredientCreate(CreateView):
    model = Ingredient
    form_class = IngredientForm
        
class IngredientDetailView(DetailView):
    model = Ingredient

class IngredientUpdate(UpdateView):
    model = Ingredient
    form_class = IngredientForm   
    
class IngredientDelete(DeleteView):
    model = Ingredient
    
    def get_success_url(self):
        return reverse('puretacodiet:ingredients')
    
#RecipeIngredients
    
class RecipeIngredientListView(ListView):
    model = RecipeIngredient
    
class RecipeIngredientCreate(CreateView):
    model = RecipeIngredient
    form_class = RecipeIngredientForm
        
class RecipeIngredientDetailView(DetailView):
    model = RecipeIngredient

class RecipeIngredientUpdate(UpdateView):
    model = RecipeIngredient
    form_class = RecipeIngredientForm   
    
class RecipeIngredientDelete(DeleteView):
    model = RecipeIngredient
    
    def get_success_url(self):
        return reverse('puretacodiet:recipe-view', kwargs={'pk': self.object.recipe.pk})
 
#DietPlans
    
class DietPlanListView(ListView):
    model = DietPlan
    
class DietPlanCreate(CreateView):
    model = DietPlan
    form_class = DietPlanForm
        
class DietPlanDetailView(DetailView):
    model = DietPlan

class DietPlanUpdate(UpdateView):
    model = DietPlan
    form_class = DietPlanForm   
    
class DietPlanDelete(DeleteView):
    model = DietPlan
    
    def get_success_url(self):
        return reverse('puretacodiet:dietplans') 
 
#Plans
    
class PlanListView(ListView):
    model = Plan
 
    
class PlanCreate(CreateView):
    model = Plan
    form_class = PlanForm
        
class PlanDetailView(DetailView):
    model = Plan

class PlanUpdate(UpdateView):
    model = Plan
    form_class = PlanForm   
    
class PlanDelete(DeleteView):
    model = Plan
    
    def get_success_url(self):
        return reverse('puretacodiet:plans')
 
#Meal

def mealadd(request, pk):
    if request.method == 'GET':
        meals = Meal.objects.all()
        return render(request, 'puretacodiet/meal_add.html', {'meals': meals})
    elif request.method == 'POST':
        plan = Plan.objects.get(pk=pk)
        for choice in request.POST['choices']:
            meal = Meal.objects.get(pk=choice)
            plan.meals.add(meal)
        plan.save()
        return render(request, 'puretacodiet/meal_add.html', {})
        
class MealListView(ListView):
    model = Meal
    
class MealCreate(CreateView):
    model = Meal
    form_class = MealForm
        
class MealDetailView(DetailView):
    model = Meal

class MealUpdate(UpdateView):
    model = Meal
    form_class = MealForm   
    
class MealDelete(DeleteView):
    model = Meal
    
    def get_success_url(self):
        return reverse('puretacodiet:meals')
 
#MealItem
    
class MealItemListView(ListView):
    model = MealItem
    
class MealItemCreate(CreateView):
    model = MealItem
    form_class = MealItemForm
     
    
    def form_valid(self, form):
        object = super(MealItemCreate, self).form_valid(form)
        print("Debug message")
        meal = Meal.objects.get(pk=self.kwargs['meal'])
        
class MealItemDetailView(DetailView):
    model = MealItem

class MealItemUpdate(UpdateView):
    model = MealItem
    form_class = MealItemForm   
    
class MealItemDelete(DeleteView):
    model = MealItem
    
    def get_success_url(self):
        return reverse('puretacodiet:mealitems')

def generateshoppinglist(request, pk):
    if request.method == 'GET':
        shoppinglist = {}
        planinstancelist = PlanInstanceList.objects.get(pk=pk)
        for planinstance in planinstancelist.planinstance.all():
            print("Plan Instance Date:", planinstance.date)
            for meal in planinstance.plan.meals.all():
                print("Meal Title:", meal.title)
                for recipe in meal.recipes.all():
                    print("Recipe Title: ", recipe.title)
                    for ingredient in recipe.ingredients.all():
                        print("Ingredient Title:", ingredient.title)
                        recipeingredient = recipe.recipeingredient_set.get(ingredient=ingredient)
                        print(ingredient.pk, recipeingredient.quantity, recipeingredient.uom)
                        if ingredient.pk in shoppinglist:
                            print("in")
                            if recipeingredient.uom in shoppinglist[ingredient.pk]:
                                shoppinglist[ingredient.pk][recipeingredient.uom] = shoppinglist[ingredient.pk][recipeingredient.uom] + recipeingredient.quantity
                            else:
                                shoppinglist[ingredient.pk][recipeingredient.uom] = recipeingredient.quantity
                        else:
                            shoppinglist[ingredient.pk] = {}
                            shoppinglist[ingredient.pk][recipeingredient.uom] = recipeingredient.quantity
        return render(request, 'puretacodiet/meal_add.html', {'meals': meals})
    elif request.method == 'POST':
        plan = Plan.objects.get(pk=pk)
        for choice in request.POST['choices']:
            meal = Meal.objects.get(pk=choice)
            plan.meals.add(meal)
        plan.save()
        return render(request, 'puretacodiet/meal_add.html', {})