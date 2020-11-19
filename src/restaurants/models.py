from django.db import models

# Create your models here.
#this class will map to the database
#remember that anytime you make changes to code here you must run manage.py makemigrations from src then manage.py migrate
#Restaurant(resID varchar(32), name, address, cuisine varchar(32), totalReviews int)
class Restaurant(models.Model):
    CUISINE_OPTIONS = (
        ('1', 'American'),
        ('2', 'Breakfast'),
        ('3', 'Chinese'),
        ('4', 'Coffee'),
        ('5', 'Pizza'),
    )
    name = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    cuisine = models.CharField(max_length=1, choices=CUISINE_OPTIONS)
    totalReviews = models.IntegerField(default=0)
