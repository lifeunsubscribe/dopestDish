from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def addRestaurant_view(request, *args,**kwargs):
    return HttpResponse("<h1>Add Restaurant with Form</h1>")

def restaurant_view(request, *args,**kwargs):
    return HttpResponse("<h1>Display Restaurant object from args</h1>")
