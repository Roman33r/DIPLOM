from django.shortcuts import render
from .models import Nedvigimost, PhotoNedvig, District, TypeNedvig, TypeUslugi, Street
from django.views.generic.base import View
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'home.html')

class Catalog(View):
    def get(self, request):
        nedvig_list = Nedvigimost.objects.all()
        type_nedvig = TypeNedvig.objects.all()
        type_uslugi = TypeUslugi.objects.all()
        districts    = District.objects.all()
        streets      = Street.objects.all()
        context = {'nedvig_list': nedvig_list,
                   'type_nedvig': type_nedvig,
                   'type_uslugi': type_uslugi,
                   'districts': districts,
                   'streets': streets}
        return render(request, 'nedvig/catalog.html', context)
    
    def post(self, request):

        print(request.POST)


        type_uslug = request.POST.get('type_uslugi')
        type_nedvigg = request.POST.get('type_nedvig')
        districts = request.POST.get('district')
        streets = request.POST.get('street')    
        prices_start = request.POST.get('Price_start')
        prices_end = request.POST.get('Price_end')

        if prices_start == '':
            prices_start = 0

        if prices_end == '':
            prices_end = 99999999    

        nedvig_list = Nedvigimost.objects.filter(Q(type_uslugi = type_uslug) & Q(type_nedvig = type_nedvigg) & Q(street = streets) & Q(district = districts) & Q(price__range=(prices_start,prices_end)))   

        context = {'nedvig_list': nedvig_list}
        return render(request, 'nedvig/catalog.html', context)

    # def objects_filter(request):
        

class NedvigDetailViews(View):

    def get(self, request, pk):
        nedvig = Nedvigimost.objects.get(id=pk)
        photo_nedvig = PhotoNedvig.objects.filter(kod_object = pk)
        print(photo_nedvig, pk)
        return render(request, 'nedvig/nedvig_page.html', {'nedvig': nedvig, 'photo_nedvig': photo_nedvig})