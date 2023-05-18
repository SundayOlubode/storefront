from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_Hi(request):
    x = 1
    y = 3
    return render(request, 'home.html', {'name': 'Sam'})