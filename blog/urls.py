from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('recipe/<slug:slug>/', views.RecipeDetail.as_view(),
         name='recipe_detail'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name='recipe_like'),
    path('edit_review/<int:review_id>/', views.EditReview.as_view(),
         name='edit_review'),
    path('delete_review/<int:review_id>/', views.DeleteReview.as_view(),
         name='delete_review'),
    path('profile/', views.ViewProfile.as_view(),
         name='profile'),
    path('edit_profile/', views.EditProfile.as_view(),
         name='edit_profile'),
]
