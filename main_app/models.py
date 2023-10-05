from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Agent(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agents_detail', kwargs={'pk': self.id})


class Listing(models.Model):
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    sqft = models.IntegerField()
    agents = models.ManyToManyField(Agent)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('detail', kwargs={'listing_id': self.id})
    

class Photo(models.Model):
    url = models.CharField(max_length=200)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for listing_id: {self.listing_id} @{self.url}"