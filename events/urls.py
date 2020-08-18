from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('add/', views.add_event, name='add_event'),
]