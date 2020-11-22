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
        ('4', 'Cafe'),
        ('5', 'Italian'),
        ('6', 'Mexican'),
        ('7', 'Bars'),
        ('8', 'Fast Food'),
        ('9', 'Ramen'),
        ('10', 'Buffet'),
        ('11', 'Thai'),
        ('12', 'Steakhouse'),
        ('13', 'Japanese'),
        ('14', 'Greek'),
        ('15', 'Indian'),
        ('16', 'Korean'),
    )
    name = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    cuisine = models.CharField(max_length=2, choices=CUISINE_OPTIONS)
    totalReviews = models.IntegerField(default=0)
