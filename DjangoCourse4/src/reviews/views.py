from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView


# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # Not necessary if using a ModelForm
#             review = Review(username=form.cleaned_data["username"],
#                             review_text=form.cleaned_data["review_text"],
#                             rating=form.cleaned_data["rating"])
#             # form.save() # If using a ModelForm
#             review.save()
#             return HttpResponseRedirect("thank-you",)
#     else:
#         form = ReviewForm()
#     return render(request, "reviews/review.html", 
#                   {"form": form})


# class ReviewView(View):
#     def get(self, request):
#         form  = ReviewForm()
#         return render(request, "reviews/review.html",
#         {"form": form})

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("thank-you")


# class ReviewView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "thank-you"


# With CreateView, forms file is not even necessary
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context


# class AllReviewsView(TemplateView):
#     # def get(self, request):
#     #     all_reviews = Review.objects.all()
#     #     return render(request, "reviews/all_reviews.html",
#     #     {"reviews": all_reviews})

#     template_name = "reviews/all_reviews.html"

#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


class AllReviewsView(ListView):
    template_name = "reviews/all_reviews.html"
    model = Review
    context_object_name = "reviews"


# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         review = Review.objects.get(pk=review_id)
#         context["review"] = review
#         return context


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
