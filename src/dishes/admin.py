from django.contrib import admin

# Register your models here.
from dishes.models import Dish
from restaurants.models import Restaurant
from reviews.models import Review
admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(Review)
