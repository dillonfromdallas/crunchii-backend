import os

from django.db import models

from photologue.models import Gallery

from recipe_backend.settings import MEDIA_ROOT
# Create your models here.


class Ingredients(models.Model):
    VEGETABLE = "veg"
    FRUIT = "fruit"
    BERRY = "berry"
    BEAN = "bean"
    NUT = "nut"
    PROTEIN = "protein"
    SEED = "seed"
    SPICE = "spice"
    GRAIN = "grain"
    BEVERAGE = "beverage"
    COOKING_LIQUID = "liquid"

    INGREDIENT_TYPE_CHOICES = (
        (VEGETABLE, "Vegetable"),
        (FRUIT, "Fruit"),
        (BERRY, "Berry"),
        (BEAN, "Bean"),
        (NUT, "Nut"),
        (PROTEIN, "Protein"),
        (SEED, "Seed"),
        (SPICE, "Spice"),
        (GRAIN, "Grain"),
        (BEVERAGE, "Beverage"),
        (COOKING_LIQUID, "Cooking Liquid"),
    )

    ingredient_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=INGREDIENT_TYPE_CHOICES, blank=True)
    calories = models.FloatField()


class Steps(models.Model):
    ingredients = models.ForeignKey(
        'Ingredients',
        on_delete=models.CASCADE,
    )
    instructions = models.TextField()


class Recipe(models.Model):
    BREAKFAST = "BREK"
    LUNCH = "L"
    DINNER = "DIN"
    SNACK = "S"
    DRINK = "BEV"
    DESSERT = "DES"

    RECIPE_TYPE_CHOICES = (
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner"),
        (SNACK, "Snack"),
        (DRINK, "Drink"),
        (DESSERT, "Dessert")
    )

    recipe_type = models.CharField(max_length=9, choices=RECIPE_TYPE_CHOICES, blank=True)
    images = models.OneToOneField(Gallery,
                                  on_delete=models.CASCADE,
                                  null=True)
    steps = models.ForeignKey(
        'Steps',
        on_delete=models.CASCADE,
    )
