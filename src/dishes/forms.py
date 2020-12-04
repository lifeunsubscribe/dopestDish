from django import forms
from .models import Dish

class dishForm(forms.ModelForm):
    class Meta:
        model = Dish
        exclude = ['numReviews']
