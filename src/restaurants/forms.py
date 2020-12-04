from django import forms
from .models import Restaurant

class restaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = [
        'totalReviews'
        ]
