from django.shortcuts import render

from .models import Listing


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def listings_index(request):
  listings = Listing.objects.all()
  return render(request, 'listings/index.html', {
    'listings': listings
})

