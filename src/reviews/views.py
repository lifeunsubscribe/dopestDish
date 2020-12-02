from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import HttpResponse
from .models import Review            #grabs the DB Posts

class ReviewListView(ListView):
    model = Review
    template_name = '/list_reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']


def addreview_view(request,*args,**kwargs):
    return HttpResponse("<h1>you are about to add a review</h1>")

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'review_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
