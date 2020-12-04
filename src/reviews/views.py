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
from dishes.models import Dish
from restaurants.models import Restaurant
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
    print(request.POST.get('dish'))

    if form.is_valid():
        form.save()
        d = request.POST.get('dish')
        r = request.POST.get('restaurant')

        obj = Dish.objects.get(id=d)
        obj.numReviews = obj.numReviews + 1  # Using an F expression to avoid race conditions
        print(obj.resID.name)
        res = Restaurant.objects.get(name=obj.resID.name)
        res.totalReviews = res.totalReviews + 1
        obj.save()
        res.save()
        form = reviewForm()
    context = {
    'form': form
    }
    return render(request,"reviews/review_form.html",context)


def process_review(request, d,r):
    dish = Dish.objects.get(title=d, resID=r)
    dish.numReviews = F('numReviews') + 1  # Using an F expression to avoid race conditions
    dish.save()



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
