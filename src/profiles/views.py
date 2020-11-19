from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup_view(request,*args,**kwargs):
    return HttpResponse("<h1>sign up (or log in?) here to become a user</h1>")
