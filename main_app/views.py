from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
    id_list = listing.agents.all().values_list('id')
    agents_listing_doesnt_have = Agent.objects.exclude(id__in=id_list)
    return render(request, 'listings/detail.html', {
        'listing': listing, 'agents': agents_listing_doesnt_have
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


# Agent Views

class AgentList(ListView):
    model = Agent


class AgentDetail(DetailView):
    model = Agent


class AgentCreate(CreateView):
    model = Agent
    fields = '__all__'


class AgentUpdate(UpdateView):
    model = Agent
    fields = '__all__'


class AgentDelete(DeleteView):
    model = Agent
    success_url = '/agents'

# Association Functions


def assoc_agent(request, listing_id, agent_id):
    Listing.objects.get(id=listing_id).agents.add(agent_id)
    return redirect('detail', listing_id=listing_id)


def de_assoc_agent(request, listing_id, agent_id):
    Listing.objects.get(id=listing_id).agents.remove(agent_id)
    return redirect('detail', listing_id=listing_id)
