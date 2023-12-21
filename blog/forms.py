from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'excerpt', 'ingredients', 'instructions', 'featured_image', 'status']