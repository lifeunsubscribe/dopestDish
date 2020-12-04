from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView

from django.http import HttpResponse
from dishes.models import Dish
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
        Dish.objects.filter(title=request.POST['dish'],restaurant=request.POST['restaurant']).update(numReviews=numReviews+1)
        form = reviewForm()
    context = {
    'form': form
    }
    return render(request,"reviews/review_form.html",context)

class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = '/'

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False

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
