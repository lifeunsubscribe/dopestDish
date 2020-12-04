"""theDopestDishProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from dishes.views import dish_view, addDish_view, search_view, search_results
from restaurants.views import restaurant_view, addRestaurant_view
from profiles.views import signup_view
from profiles import views as profile_views
from reviews.views import ReviewListView, ReviewCreateView, addreview_view, review_details_view
from reviews.models import Review
#from locations.views import

def home_view(request,*args,**kwargs):
    print(request.user.is_authenticated)
    reviewList = Review.objects.all()
    context = {
    'reviewList':reviewList
    }
    return render(request,"home.html", context)

urlpatterns = [
    path('', home_view, name='home'),     #display recent reviews, short blurb, login/signup options, to link to home.html we add name='home'
    path('admin/', admin.site.urls),    #interface to manage database objects
    path('search/', search_view, name='search'),       #search bar for restaurants or dishes with predictive text and/or options for adding to database
    path('search/<str:t>/',search_results, name='search_results'),

    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('profile/', profile_views.profile, name='profile'),

    path('list_reviews/', ReviewListView.as_view(), name='review-list'),
    path('review/new/', addreview_view, name='review-create'),
    path('review/details', review_details_view, name='review-details'),

    #path('list_dishs/', ReviewListView.as_view(), name='review-list'),
    path('dish/new/', addDish_view, name='dish-create'),
    path('dish/<int:id>/', dish_view, name='dish-details')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
