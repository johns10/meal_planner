from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'puretacodiet'
urlpatterns = [
    url(r'^$', views.index, name='index'),    
    #Taco Recipes
    url(r'^taco/create/$', views.RecipeCreate.as_view(), name='recipe-create', ),
    url(r'^taco/(?P<pk>[0-9]+)/$', views.RecipeDetailView.as_view(), name='recipe-view'),
    url(r'^taco/(?P<slug>[\w-]+)/$', views.RecipeDetailView.as_view(), name='recipe-view'),
    url(r'^taco/(?P<pk>[0-9]+)/edit/$', views.RecipeUpdate.as_view(), name='recipe-update'),
    url(r'^taco/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name='recipe-delete'), 
    url(r'^tacos/', views.RecipeListView.as_view(), name='recipes'),
    #Recipe Ingredients
    url(r'^recipeingredient/create/$', views.RecipeIngredientCreate.as_view(), name='recipeingredient-create'),
    url(r'^recipeingredient/(?P<pk>[0-9]+)/$', views.RecipeIngredientDetailView.as_view(), name='recipeingredient-view'),
    url(r'^recipeingredient/(?P<slug>[\w-]+)/$', views.RecipeIngredientDetailView.as_view(), name='recipeingredient-view'),
    url(r'^recipeingredient/(?P<pk>[0-9]+)/edit/$', views.RecipeIngredientUpdate.as_view(), name='recipeingredient-update'),
    url(r'^recipeingredient/(?P<pk>[0-9]+)/delete/$', views.RecipeIngredientDelete.as_view(), name='recipeingredient-delete'), 
    url(r'^recipeingredients/', views.RecipeIngredientListView.as_view(), name='recipeingredients'),
    #Ingredients
    url(r'^ingredient/create/$', views.IngredientCreate.as_view(), name='ingredient-create'),
    url(r'^ingredient/(?P<pk>[0-9]+)/$', views.IngredientDetailView.as_view(), name='ingredient-view'),
    url(r'^ingredient/(?P<slug>[\w-]+)/$', views.IngredientDetailView.as_view(), name='ingredient-view'),
    url(r'^ingredient/(?P<pk>[0-9]+)/edit/$', views.IngredientUpdate.as_view(), name='ingredient-update'),
    url(r'^ingredient/(?P<pk>[0-9]+)/delete/$', views.IngredientDelete.as_view(), name='ingredient-delete'), 
    url(r'^ingredients/', views.IngredientListView.as_view(), name='ingredients'),
    #DietPlans
    url(r'^dietplan/create/$', views.DietPlanCreate.as_view(), name='dietplan-create'),
    url(r'^dietplan/(?P<pk>[0-9]+)/$', views.DietPlanDetailView.as_view(), name='dietplan-view'),
    url(r'^dietplan/(?P<slug>[\w-]+)/$', views.DietPlanDetailView.as_view(), name='dietplan-view'),
    url(r'^dietplan/(?P<pk>[0-9]+)/edit/$', views.DietPlanUpdate.as_view(), name='dietplan-update'),
    url(r'^dietplan/(?P<pk>[0-9]+)/delete/$', views.DietPlanDelete.as_view(), name='dietplan-delete'), 
    url(r'^dietplans/', views.DietPlanListView.as_view(), name='dietplans'),
    #Plans
    url(r'^plan/create/$', views.PlanCreate.as_view(), name='plan-create'),
    url(r'^plan/(?P<pk>[0-9]+)/$', views.PlanDetailView.as_view(), name='plan-view'),
    url(r'^plan/(?P<slug>[\w-]+)/$', views.PlanDetailView.as_view(), name='plan-view'),
    url(r'^plan/(?P<pk>[0-9]+)/edit/$', views.PlanUpdate.as_view(), name='plan-update'),
    url(r'^plan/(?P<pk>[0-9]+)/delete/$', views.PlanDelete.as_view(), name='plan-delete'), 
    url(r'^plans/', views.PlanListView.as_view(), name='plans'),
    #Meal
    url(r'^meal/create/$', views.MealCreate.as_view(), name='meal-create'),
    url(r'^meal/add/(?P<pk>[0-9]+)/$', views.mealadd, name='meal-add'), 
    url(r'^meal/(?P<pk>[0-9]+)/$', views.MealDetailView.as_view(), name='meal-view'),
    url(r'^meal/(?P<slug>[\w-]+)/$', views.MealDetailView.as_view(), name='meal-view'),
    url(r'^meal/(?P<pk>[0-9]+)/edit/$', views.MealUpdate.as_view(), name='meal-update'),
    url(r'^meal/(?P<pk>[0-9]+)/delete/$', views.MealDelete.as_view(), name='meal-delete'), 
    url(r'^meals/', views.MealListView.as_view(), name='meals'),
    #MealItem
    url(r'^mealitem/create/(?P<meal>\d+)/$', views.MealItemCreate.as_view(), name='mealitem-create'),
    url(r'^mealitem/(?P<pk>[0-9]+)/$', views.MealItemDetailView.as_view(), name='mealitem-view'),
    url(r'^mealitem/(?P<slug>[\w-]+)/$', views.MealItemDetailView.as_view(), name='mealitem-view'),
    url(r'^mealitem/(?P<pk>[0-9]+)/edit/$', views.MealItemUpdate.as_view(), name='mealitem-update'),
    url(r'^mealitem/(?P<pk>[0-9]+)/delete/$', views.MealItemDelete.as_view(), name='mealitem-delete'), 
    url(r'^mealitems/', views.MealItemListView.as_view(), name='mealitems'),
]
