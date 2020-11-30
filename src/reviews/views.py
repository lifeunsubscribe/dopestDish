from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Review            #grabs the DB Posts

class ReviewListView(ListView):
    model = Review
    template_name = '/list_reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'review_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

