from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('listings/', views.listings_index, name='index'),
    path('listings/<int:listing_id>/', views.listings_detail, name='detail'),
    path('listings/create/', views.ListingCreate.as_view(), name='listings_create'),
    path('listings/<int:pk>/update/', views.ListingUpdate.as_view(), name='listings_update'),
    path('listings/<int:pk>/delete/', views.ListingDelete.as_view(), name='listings_delete'),
    # Agent URLS Below
    path('agents/', views.AgentList.as_view(), name='agents_index'),
    path('agents/<int:pk>/', views.AgentDetail.as_view(), name='agents_detail'),
    path('agents/create/', views.AgentCreate.as_view(), name='agents_create'),
    path('agents/<int:pk>/update/', views.AgentUpdate.as_view(), name='agents_update'),
    path('agents/<int:pk>/delete/', views.AgentDelete.as_view(), name='agents_delete'),
    #Association URLS Below
    path('listings/<int:listing_id>/assoc_agent/<int:agent_id>/', views.assoc_agent, name='assoc_agent'),
    path('listings/<int:listing_id>/de_assoc_agent/<int:agent_id>/', views.de_assoc_agent, name='de_assoc_agent'),
]
