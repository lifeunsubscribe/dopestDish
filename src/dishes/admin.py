from django.contrib import admin

# Register your models here.
from dishes.models import Dish
from restaurants.models import Restaurant
admin.site.register(Dish)
admin.site.register(Restaurant)
