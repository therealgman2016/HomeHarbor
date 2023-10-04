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

def listings_detail(request, listing_id):
   listing = Listing.objects.get(id=listing_id)
   return render(request, 'listings/details.html', { 
      'listing': listing 
})