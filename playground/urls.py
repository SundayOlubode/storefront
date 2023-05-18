from django.urls import path
from . import views

urlpatterns = [
    path('say_hi/', views.say_Hi)
]