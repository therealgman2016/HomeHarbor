from django.db import models
from django.urls import reverse

# Create your models here.

class Agent(models.Model):
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'agent_id': self.id})
  

class Listing(models.Model):
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    sqft = models.IntegerField()
    agents = models.ManyToManyField(Agent)

    def __str__(self):
        return self.address
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'listing_id': self.id})

