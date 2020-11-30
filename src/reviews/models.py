from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})