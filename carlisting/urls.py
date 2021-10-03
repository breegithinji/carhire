from django.urls import path
from django.urls.conf import include
from . import views

# app_name = 'carlistings'
urlpatterns = [
    path('',views.index, name='index'),
    path('allcars.html', views.all_cars, name='allcars'),
    path('<int:car_id>', views.car_details, name='cardetails'),
    path('toyotas.html', views.toyota_cars, name='toyotas')
] 

