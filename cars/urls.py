from django.urls import path,include
from cars import views

urlpatterns = [
    path("",views.cars,name="cars"),# this will link the cars method in the view.py file
]