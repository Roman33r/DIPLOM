from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def catalog(request):
    return render(request, 'nedvig/catalog.html')