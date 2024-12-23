from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar, name='calendar'),
    path('workers/', views.workers, name='workers'),
    path('worker/<int:id>/', views.worker_detail, name='worker_detail'),
    path('worker/<int:id>/edit', views.edit_worker, name='edit_worker'),
    path('create_event/<str:date>/', views.create_event, name='create_event'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]