from django import forms
from django.utils.text import slugify
from django.shortcuts import redirect
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'excerpt', 'ingredients',
                   'instructions', 'featured_image']

    featured_image = forms.ImageField(required=False)

    def save(self, commit=True):
        instance = super(RecipeForm, self).save(commit = False)
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance

