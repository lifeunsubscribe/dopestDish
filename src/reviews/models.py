from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from dishes.models import Dish

class Review(models.Model):
    stars = [
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(choices=stars)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "reviews"
        constraints = [
            models.UniqueConstraint(fields=['author','dish','restaurant'], name='oneVote')
        ]



    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})
