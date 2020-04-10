from django.db import models
from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

OUNCE = 'OZ'
EACH = 'EA'
GALLON = 'GAL'
QUART = 'QT'
FLUIDOUNCE = 'FLOZ'
POUND = 'LB'
LITER = 'L'
UOM_CHOICES = (
    ('OZ', 'Ounce'),
    ('EA', 'Each'),
    ('GAL','Gallon'),
    ('QT','Quart'),
    ('FLOZ','Fluid Ounce'),
    ('LB','Pound'),
    ('L','Liter'),
)

class Vendor(models.Model):
    name = models.TextField(help_text="Name of the Vendor.")

class UserProfile(models.Model):
    Louisville = 'Louisville'
    CITY_CHOICES = (
        ('Louisville', 'Louisville'),
    )
    Kentucky = 'KY'
    STATE_CHOICES = (
        ('KY', 'Kentucky'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=25, choices = CITY_CHOICES, default = Louisville)
    state = models.CharField(max_length=4 choices = STATE_CHOICES, default = Kentucky)
    zip = models.IntegerField()
    homephone = models.CharField(max_length=10)
    mobilephone = models.CharField(max_length=10)

class ExternalCredential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    username = models.TextField(help_text="enter your username")
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

class Ingredient(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    photo = models.ImageField(blank=True, upload_to="ingredient_photos")
    calories = models.DecimalField(help_text="Number of calories in this ingredient, per measurement", max_digits = 5, decimal_places = 2)
    protein = models.DecimalField(help_text="Grams of carbohydrates in this ingredient, per measurement", max_digits = 5, decimal_places = 2)
    fat = models.DecimalField(help_text="Grams of fat in this ingredient, per measurement", max_digits = 5, decimal_places = 2)
    carbohydrates = models.DecimalField(help_text="Grams of carbohydrates in this ingredient, per measurement", max_digits = 5, decimal_places = 2)
 
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/puretacodiet/ingredient/%s/" % self.slug
        
    def get_success_url(self):
        return reverse('puretacodiet:ingredients')#Better Implementation
        
# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    photo = models.ImageField(blank=True, upload_to="recipe_photos")
    info = models.TextField(help_text="enter information about the recipe")
    servings = models.IntegerField(help_text="enter total number of servings")
    weight = models.DecimalField(help_text="Total weight of 1 serving, in ounces", max_digits = 5, decimal_places = 2)
    calories = models.DecimalField(help_text="Number of calories in this recipe, per serving", max_digits = 5, decimal_places = 2)
    protein = models.DecimalField(help_text="Grams of carbohydrates in this recipe, per serving", max_digits = 5, decimal_places = 2)
    fat = models.DecimalField(help_text="Grams of fat in this recipe, per serving", max_digits = 5, decimal_places = 2)
    carbohydrates = models.DecimalField(help_text="Grams of carbohydrates in this recipe, per serving", max_digits = 5, decimal_places = 2)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    directions = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pub_date', 'title']

    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/puretacodiet/taco/%s/" % self.slug
        
    def get_success_url(self):
        return reverse('puretacodiet:recipes')#Better Implementation
        
    def calculate_nutrition(self):
        print("Recalculating nutrition")
        self.calories = 0
        self.protein = 0
        self.fat = 0
        self.carbohydrates = 0
        self.weight = 0
        for ri in self.recipeingredient_set.all():
            self.calories += (ri.ingredient.calories * ri.quantity)
            self.protein += (ri.ingredient.protein * ri.quantity)
            self.fat += (ri.ingredient.fat * ri.quantity)
            self.carbohydrates += (ri.ingredient.carbohydrates * ri.quantity)
            self.weight += (ri.quantity)
        self.save()

class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.DecimalField(help_text="Quantity of the ingredient in the amount specified.", max_digits = 3, decimal_places = 2)
    uom = models.CharField(max_length=4 choices = UOM_CHOICES, default = OUNCE)
    
    def get_absolute_url(self):
        return "/puretacodiet/recipeingredient/%s/" % self.pk
        
class DietPlan(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField(help_text="enter information about the recipe")
    quantity = models.DecimalField(help_text="Number of Tacos.", max_digits = 3, decimal_places = 2)
        
    def get_absolute_url(self):
        return "/puretacodiet/dietplan/%s/" % self.slug

    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title
        
class Meal(models.Model):
    title = models.CharField(max_length=250)
    recipes = models.ManyToManyField(Recipe, through='MealItem')
    
    def get_absolute_url(self):
        return "/puretacodiet/meals"
        
    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title
        
class MealItem(models.Model):
    meal = models.ForeignKey(Meal)
    quantity = models.DecimalField(help_text="Number of servings of this taco in the recipe.", max_digits = 2, decimal_places = 1)
    recipe = models.ForeignKey(Recipe)
    
    def get_absolute_url(self):
        return "/puretacodiet/mealitems"
        
class Plan(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField(help_text="enter information about the recipe")
    dietplan = models.ForeignKey(DietPlan, blank="True", null="True")
    meals = models.ManyToManyField(Meal)
    
    def get_absolute_url(self):
        return "/puretacodiet/plan/%s/" % self.slug

    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.title
        
class PlanInstance(models.Model):
    date = models.DateField()
    plan = models.ForeignKey(Plan, blank="True", null="True")

class PlanInstanceList(models.Model):
    planinstance = models.ManyToManyField(PlanInstance)
    
    
class MealInstance(models.Model):
    datetime = models.DateTimeField()
    meal = models.ForeignKey(Meal, blank="True", null="True")
    
    
class Product(models.Model):
    UNIT = 'UNIT'
    WEIGHT = 'WEIGHT'
    BY_CHOICES = (
        ('UNIT', 'UNIT'),
        ('WEIGHT', 'WEIGHT'),
    )
    vendor = models.ForeignKey(Vendor, blank="True", null="True")
    sku = models.TextField(help_text="Quantity of this product.")
    name = models.CharField(max_length=250)
    regularprice = models.DecimalField(help_text="Regular Price.", max_digits = 4, decimal_places = 2)
    saleprice = models.DecimalField(help_text="Sale Price.", max_digits = 4, decimal_places = 2)
    offerquantity = models.IntegerField()
    offerprice = models.DecimalField(help_text="Offer Price.", max_digits = 4, decimal_places = 2)
    soldby = models.CharField(max_length=8, choices = BY_CHOICES, default = UNIT)
    orderby = models.CharField(max_length=8, choices = BY_CHOICES, default = UNIT)

    def getproductinfo(self, product):
        self.regularprice = product['regularPrice']
        self.saleprice = product['salePrice']
        self.offerquentity = product['offerQuantity']
        self.offerprice = product['offerPrice']
        self.soldby = product['soldBy']
        self.orderby = product['orderBy']


class ProductQuantity(models.Model):    
    product = models.ForeignKey(Product, blank="False", null="False")
    uom = models.CharField(max_length=4 choices = UOM_CHOICES, default = OUNCE)
    quantity = models.IntegerField()
