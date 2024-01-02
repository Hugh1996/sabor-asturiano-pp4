from django import forms
from django.utils.text import slugify
from django.shortcuts import redirect
from .models import Review, Recipe


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'excerpt', 'ingredients', 'instructions',
                  'featured_image']

    