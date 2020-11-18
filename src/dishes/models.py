from django.db import models

# Create your models here.
#this class will map to the database
#remember that anytime you make changes to code here you must run manage.py makemigrations from src then manage.py migrate
#MenuItem(name varchar(50), resID varchar(32), price float, description varchar(150), numReviews int)
#from .models import Restaurant

class Dish(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    #resID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    description = models.TextField(blank=False, null=False)
    numReviews = models.IntegerField(default=0)
