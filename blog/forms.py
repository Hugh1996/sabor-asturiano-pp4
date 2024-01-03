from django import forms
from django.utils.text import slugify
from django.shortcuts import redirect
from .models import Review, Recipe, UserProfile


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'excerpt', 'ingredients', 'instructions',
                  'featured_image']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
