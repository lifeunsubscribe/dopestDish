from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from .models import Dish


# Create your views here.
def addDish_view(request,*args,**kwargs):
    return HttpResponse("<h1>Add Dish with Form</h1>")

def dish_view(request,*args,**kwargs):
    return HttpResponse("<h1>Display Dish object from args</h1>")

def search_view(request,*args,**kwargs):
    return render(request, 'dishes/search.html')
