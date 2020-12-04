from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Dish
from reviews.models import Review
from .forms import dishForm


# Create your views here.
def addDish_view(request,*args,**kwargs):
    form = dishForm(request.POST or None)
    #dish = request.POST.get('dish')
    print(request.method)
    if form.is_valid():
        form.save()
        form = dishForm()
    context = {
    'form': form
    }
    if request.method == "GET":
        return render(request,"dishes/add_dish.html",context)
    else:
        return render(request,"dishes/dish_details.html",context)

def dish_view(request,id):
    obj = Dish.objects.get(id=id)
    reviewList = []
    avgRating = 0
    i = 0
    if Review.objects.filter(dish=obj.id).exists():
            reviewList = Review.objects.filter(dish=obj.id)

    for r in reviewList:
        i+=1
        avgRating += r.rating

    avgRating /= i

    context = {
    'object':obj,
    'reviewList':reviewList,
    'avgRating':avgRating
    }
    print(obj)
    print(reviewList[0].dish)
    return render(request,"dishes/dish_details.html",context)

class searchBar(forms.ModelForm):
    #dish = forms.CharField(label='',required=False)
    class Meta:
        model = Review

        fields = [
        'dish'
        ]

def search_view(request):
    #obj = Dish.objects.get(title=t)
    search = searchBar(request.GET or None)
    print(request)
    print(dir(request))
    #print(dir(search))


    context = {
    'search': search,
    'object':object
    }
    return render(request, 'dishes/search.html',context)

def search_results(request,t):
    #object = Dish.objects.get(title=t)
    context = {
    'search': search
    }
    return render(request,'dishes/search.html',context)


#<str:t>/
