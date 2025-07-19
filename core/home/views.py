from django.shortcuts import render
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
def home(request):
    """
    Render the home page.
    """
    return render(request, "home/index.html")