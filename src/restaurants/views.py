from django.shortcuts import render
from django.http import HttpResponse
from .forms import restaurantForm
from .models import Restaurant
from django.views.generic import TemplateView, ListView
# Create your views here.


def addRestaurant_view(request, *args,**kwargs):
    form = restaurantForm(request.POST or None)
    #dish = request.POST.get('dish')
    object = Restaurant()
    print(request.method)
    if form.is_valid():
        form.save()
        d = form.cleaned_data
        print(request.POST.get('name'))
        #print(request.POST.get['name'])
        #object = Restaurant.objects.filter(name=request.POST.get['name'])
        form = restaurantForm()

    context = {
    'form': form,
    'object':object
    }

    return render(request,"restaurants/add_rest.html",context)


class RestaurantDetailsView(ListView):
    model = Restaurant
    template_name = 'restaurants/rest_details.html'


    def get_queryset(self): # new
        query = self.request.POST.get('q')
        object= Dish.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
        return object

def restaurant_view(request, *args,**kwargs):
    return HttpResponse("<h1>Display Restaurant object from args</h1>")
