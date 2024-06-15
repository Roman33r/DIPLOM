from django.shortcuts import render
from .models import Nedvigimost
from django.views.generic.base import View
# Create your views here.

def home(request):
    return render(request, 'home.html')

class Catalog(View):
    def get(self, request):
        nedvig_list = Nedvigimost.objects.all()
        context = {'nedvig_list': nedvig_list}

        return render(request, 'nedvig/catalog.html', context)

def nedvig_page(request):
    return render(request, 'nedvig/nedvig_page.html')