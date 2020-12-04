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
from profiles.models import User
from .models import Review            #grabs the DB Posts
from .forms import reviewForm
class ReviewListView(ListView):
    model = Review
    template_name = '/list_reviews.html'
    context_object_name = 'reviews'
    ordering = ['-date_posted']


def addreview_view(request,*args,**kwargs):
    r = Review(author=request.user)
    form = reviewForm(request.POST or None,instance=r)
    dish = request.POST.get('dish')

    if form.is_valid():
        form.save()
        form = reviewForm()
    context = {
    'form': form
    }
    return render(request,"reviews/review_form.html",context)



def review_details_view(request,*args,**kwargs):
    r = Review(author=request.user)
    form = reviewForm(request.POST or None,instance=r)
    dish = request.POST.get('dish')

    if form.is_valid():
        form.save()
        form = reviewForm()
    context = {
    'form': form
    }
    return render(request,"reviews/review_form.html",context)




class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['title', 'review_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
