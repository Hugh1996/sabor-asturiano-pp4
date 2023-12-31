from django.contrib import admin
from .models import Recipe, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'is_approved')
    search_fields = ['title', 'content']
    summernote_fields = ('ingredients', 'instructions')
    actions = ['approve_recipes']

    def approve_recipes(self, request, queryset):
        queryset.update(is_approved=True)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')
