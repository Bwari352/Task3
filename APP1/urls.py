from django.contrib import admin
from django.urls import path


from.import views

app_name = 'APP1'

urlpatterns = [

    path('', views.home, name='home'),

    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

    # path('testimonials/', views.testimonials, name='testimonials'),

    path('contact/', views.contact, name='contact'),

    path('insert_data/', views.insert_data, name='insert_data'),


]
