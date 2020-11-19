from django.db import models

from restaurants.models import Restaurant

class Location(models.Model):
    address = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    name = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    numReviews = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name','address'], name='uniqueLocation')
        ]
