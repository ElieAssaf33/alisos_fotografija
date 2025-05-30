from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('prices',views.prices,name='prices'),
    path('contacts',views.contacts,name='contacts'),
    path('wedding',views.wedding,name='wedding'),
    path('street',views.street,name='street'),
    path('portrait',views.portrait,name='portrait'),
    path('nature',views.nature,name='nature'),
    path('family',views.family,name='family'),
    path('events',views.events,name='events'),
    path('about', views.about, name='about'),
    path('reviews', views.reviews, name='reviews'),
    path('submit-review', views.submit_review, name='submit_review'),
]