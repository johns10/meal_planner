from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from puretacodiet.models import Recipe, RecipeIngredient

@receiver([post_save, post_delete], sender=RecipeIngredient)
def recipe_ingredient_change(sender, **kwargs):
    print("Got post save signal")
    kwargs['instance'].recipe.calculate_nutrition()
    