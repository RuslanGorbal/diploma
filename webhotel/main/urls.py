from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('about_standart', views.about_standart, name='about_standart'),
    path('about_deluxe', views.about_deluxe, name='about_deluxe'),
    path('about_family', views.about_family, name='about_family'),
    path('about_luxe', views.about_luxe, name='about_luxe'),
    path('about_proluxe', views.about_proluxe, name='about_proluxe'),
    path('about_business', views.about_business, name='about_business'),
    path('services', views.services, name='services'),
    path('create', views.create, name='create'),
    path('create_receipt', views.create_receipt, name='create_receipt')
]

