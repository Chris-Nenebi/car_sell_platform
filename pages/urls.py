
from django.urls import path,include
from pages import views

urlpatterns = [
    path("",views.home,name="home"),# this will link the home method in the view.py file
    path("about",views.about,name="about"), # this will link the about method in the view.py file
    path("services",views.services,name="services"),
    path("contact",views.contact,name="contact"),
]