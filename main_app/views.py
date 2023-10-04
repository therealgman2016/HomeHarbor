from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Listing, Agent


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
    return render(request, 'listings/detail.html', {
        'listing': listing
    })


class ListingCreate(CreateView):
    model = Listing
    fields = ['price', 'description', 'sqft', 'address']


class ListingUpdate(UpdateView):
    model = Listing
    fields = ['price', 'description', 'sqft']


class ListingDelete(DeleteView):
    model = Listing
    success_url = '/listings'

def listings_detail(request, listing_id):
  listing = Listing.objects.get(id=listing_id)
  id_list = listing.agents.all().values_list('id')
  agents_listing_doesnt_have = Agent.objects.exclude(id__in=id_list)
  return render(request, 'listings/detail.html', {
    'listing': listing,
    'agents': agents_listing_doesnt_have
  })