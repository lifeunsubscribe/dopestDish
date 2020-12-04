from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Dish
from reviews.models import Review
from .forms import dishForm


# Create your views here.
def addDish_view(request,*args,**kwargs):
    form = dishForm(request.POST or None)
    #dish = request.POST.get('dish')
    object = Dish()
    print(request.method)
    if form.is_valid():
        form.save()
        form = dishForm()

    context = {
    'form': form,
    'object':object
    }
    return render(request,"dishes/add_dish.html",context)

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
    dishList = Dish.objects.all()
    search = searchBar(request.GET or None)
    print(request.GET)
    print(request.GET.urlencode())
    #print(dir(search))

    print(request.GET['dish'])
    dishList = Dish.objects.filter(id=request.GET['dish'])
    #print(object[0].title)
    context = {
    'search': search,
    'dishList':dishList
    }
    return render(request, 'dishes/search.html',context)


class SearchResultsView(ListView):
    model = Dish
    template_name = 'dishes/search.html'


    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list= Dish.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
        return object_list




#<str:t>/
