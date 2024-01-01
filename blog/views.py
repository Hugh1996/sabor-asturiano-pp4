from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Review
from .forms import ReviewForm, RecipeForm


class HomePage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipe.html'
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        reviews = recipe.reviews.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "reviews": reviews,
                "reviewed": False,
                "liked": liked,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        reviews = recipe.reviews.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.recipe = recipe
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "reviews": reviews,
                "reviewed": True,
                "liked": liked,
                "review_form": ReviewForm()
            
            },
        )


class RecipeLike(View):

    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class EditReview(View):

    def get(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        form = ReviewForm(instance=review)
        return render(request, 'edit_review.html', {'form': form,
                                                    'review': review})

    def post(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            messages.success(request, 'Review edited successfully!')
            return redirect('recipe_detail', slug=review.recipe.slug)
        else:
            messages.error(
                request, 'Error editing the review. Please check the form.')
        return render(request, 'edit_review.html', {'form': form,
                                                    'review': review})


class DeleteReview(View):

    def get(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        return render(request, 'delete_review.html', {'review': review})

    def post(self, request, review_id, *args, **kwargs):
        review = get_object_or_404(Review, id=review_id)
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('recipe_detail', slug=review.recipe.slug)


class AddRecipe(View):

    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        return render(request, 'add_recipe.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.is_approved = False
            recipe.save()
            return redirect('recipe_detail', slug=recipe.slug)
        return render(request, 'add_recipe.html', {'form': form,
                      'awaiting_approval': False})
