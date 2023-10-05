from django.contrib import admin
from .models import Listing
from .models import Agent
from .models import Photo

admin.site.register(Listing)

admin.site.register(Agent)

admin.site.register(Photo)