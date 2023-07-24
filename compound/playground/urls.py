from django.urls import path 
from . import views


# URLConfiguration model
urlpatterns = [
    path('hello/', views.say_hello)
]
