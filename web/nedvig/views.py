from django.shortcuts import render
from .models import Nedvigimost, PhotoNedvig, District, TypeNedvig, TypeUslugi, Street, Zayavki
from django.views.generic.base import View
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
from django.urls import reverse_lazy
# Create your views here.

class Home(View):
    def get(self, request):
        type_uslug = TypeUslugi.objects.all()
        context = {'type_uslug':type_uslug}
        return render(request, 'home.html', context)
    
    def post(self, request):
        print("-"*20)
        print(request.POST)
        tu = TypeUslugi.objects.all().filter(pk=request.POST.get('type_uslugi')).first()
        print("-"*20)
        print(tu)
        Zayavka = Zayavki.objects.create(FIO = request.POST.get('FIO'), Phone = request.POST.get('Phone'), type_uslugi = tu)
        return reverse_lazy('home')
class Catalog(View):
    def get(self, request):
        nedvig_list = Nedvigimost.objects.filter(publish = True)

        paginator = Paginator(nedvig_list, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        type_nedvig = TypeNedvig.objects.all()
        type_uslugi = TypeUslugi.objects.all()
        districts    = District.objects.all()
        streets      = Street.objects.all()
        context = {'page_obj': page_obj,
                   'nedvig_list': nedvig_list,
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
    

        nedvig_list = Nedvigimost.objects.filter(Q(type_uslugi = type_uslug) | Q(type_nedvig = type_nedvigg) | Q(street = streets) | Q(district = districts) | Q(price__range=(prices_start,prices_end)))   

        context = {'nedvig_list': nedvig_list}
        return render(request, 'nedvig/catalog.html', context)

    # def objects_filter(request):
        

class NedvigDetailViews(View):

    def get(self, request, pk):
        nedvig = Nedvigimost.objects.get(id=pk)
        photo_nedvig = PhotoNedvig.objects.filter(kod_object = pk)
        count_ph = []
        for i in range(len(photo_nedvig)):
            count_ph.append(i+1)

        

        price = str(nedvig.price)
        if len(price) == 6:
            strp = price[:3] + ' ' + price[3:]     
        elif len(price) == 7:
            strp = price[:1] + ' ' + price[1:]
            strp = strp[:5] + ' ' + strp[5:]
        elif len(price) == 8: 
            strp = price[:2] + ' ' + price[2:]
            strp = strp[:6] + ' ' + strp[6:]
            strp = strp[:10] + ' ' + strp[10:]   
        

        nedvig.price = strp
        nedvig.date_public = nedvig.date_public.strftime('%d.%m.%Y')
        print(photo_nedvig, count_ph)
        return render(request, 'nedvig/nedvig_page.html', {'nedvig': nedvig, 'photo_nedvig': photo_nedvig, 'count_ph':count_ph})