from django.contrib import admin
from .models import Listing
from .models import Agent

admin.site.register(Listing)

admin.site.register(Agent)