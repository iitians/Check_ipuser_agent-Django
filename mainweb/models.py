from django.db import models
from django.urls import reverse

class CarDetail(models.Model):
    vin = models.CharField(max_length=10)
    plates = models.CharField(max_length=6)
    date = models.CharField(max_length=10)
    ip = models.GenericIPAddressField(null=True)
    location = models.CharField(max_length=4, blank=True)
    user_agent = models.TextField(null=True)


    def __str__(self):
        return self.plates
    
    def get_absolute_url(self):
        return reverse('home')