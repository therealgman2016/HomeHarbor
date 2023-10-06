import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Listing, Agent, Photo



def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def listings_index(request):
    listings = Listing.objects.filter(user=request.user)
    return render(request, 'listings/index.html', {
        'listings': listings
    })


def listings_index_all(request):
    listings = Listing.objects.all()
    return render(request, 'listings/indexAll.html', {
        'listings': listings
})

@login_required
def listings_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    id_list = listing.agents.all().values_list('id')
    agents_listing_doesnt_have = Agent.objects.exclude(id__in=id_list)
    return render(request, 'listings/detail.html', {
        'listing': listing, 'agents': agents_listing_doesnt_have
    })


def listings_detail_show(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    id_list = listing.agents.all().values_list('id')
    agents_listing_doesnt_have = Agent.objects.exclude(id__in=id_list)
    return render(request, 'listings/detail_view.html', {
        'listing': listing, 'agents': agents_listing_doesnt_have
    })

class ListingCreate(LoginRequiredMixin, CreateView):
    model = Listing
    fields = ['address', 'price', 'description', 'sqft']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListingUpdate(LoginRequiredMixin, UpdateView):
    model = Listing
    fields = ['price', 'description', 'sqft']


class ListingDelete(LoginRequiredMixin, DeleteView):
    model = Listing
    success_url = '/listings'


# Agent Views

class AgentList(ListView):
    model = Agent


class AgentDetail(LoginRequiredMixin, DetailView):
    model = Agent


class AgentCreate(LoginRequiredMixin, CreateView):
    model = Agent
    fields = '__all__'


class AgentUpdate(LoginRequiredMixin, UpdateView):
    model = Agent
    fields = '__all__'


class AgentDelete(LoginRequiredMixin, DeleteView):
    model = Agent
    success_url = '/agents'

# Association Functions

@login_required
def assoc_agent(request, listing_id, agent_id):
    Listing.objects.get(id=listing_id).agents.add(agent_id)
    return redirect('detail', listing_id=listing_id)

@login_required
def de_assoc_agent(request, listing_id, agent_id):
    Listing.objects.get(id=listing_id).agents.remove(agent_id)
    return redirect('detail', listing_id=listing_id)

@login_required
def add_photo(request, listing_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to listing_id or listing (if you have a listing object)
            Photo.objects.create(url=url, listing_id=listing_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', listing_id=listing_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)