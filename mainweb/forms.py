from django import forms
from .models import CarDetail

class get_car_data(forms.ModelForm):
    class Meta:
        model = CarDetail
        fields = ['vin', 'plates', 'date']