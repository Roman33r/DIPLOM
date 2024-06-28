from django.shortcuts import render
from .models import Nedvigimost, PhotoNedvig, District, TypeNedvig, TypeUslugi, Street, Zayavki
from django.views.generic.base import View
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

#Домашняя страница
class Home(View):
    def get(self, request):
        type_uslug = TypeUslugi.objects.all()
        context = {'type_uslug':type_uslug}
        return render(request, 'home.html', context)
    
    def post(self, request):
        tu = TypeUslugi.objects.all().filter(pk=request.POST.get('type_uslugi')).first()
        Zayavka = Zayavki.objects.create(FIO = request.POST.get('FIO'), Phone = request.POST.get('Phone'), type_uslugi = tu)
        return redirect('home')

#Каталог недвижимости    
class Catalog(View):

    def get(self, request):

        nedvig_list = Nedvigimost.objects.filter(publish = True)
        short = []
        for nedvig in nedvig_list:
            title = nedvig.name
            strlen = len(title)
            if strlen > 56:
                n = strlen - 56
                nedvig.name = title[:-n] + '...'
            if strlen < 31:
                short.append(nedvig.pk)
            price = str(nedvig.price)
            strp = ValidPrice(price)   
            nedvig.price = strp

        paginator = Paginator(nedvig_list, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        print(page_obj)
        print(paginator)
        print(page_number)

        type_nedvig = TypeNedvig.objects.all()
        type_uslugi = TypeUslugi.objects.all()
        districts    = District.objects.all()
        streets      = Street.objects.all()

        context = {'page_obj': page_obj,
                   'nedvig_list': nedvig_list,
                   'type_nedvig': type_nedvig,
                   'type_uslugi': type_uslugi,
                   'districts': districts,
                   'streets': streets,
                   'short': short}
        return render(request, 'nedvig/catalog.html', context)
    
    def post(self, request):

        type_uslugf = request.POST.get('type_uslugi')
        type_nedvigf = request.POST.get('type_nedvig')
        districtf = request.POST.get('district')
        streetf = request.POST.get('street')    
        prices_start = request.POST.get('Price_start')
        prices_end = request.POST.get('Price_end')
        komnat1 = request.POST.get('komant1')
        komnat2 = request.POST.get('komant2')
        komnat3 = request.POST.get('komant3')
        komnat4 = request.POST.get('komant4')
        komnat5 = request.POST.get('komant5')
        Studia = request.POST.get('Studia')
        print("-"*30)
        print(type_uslugf, type_nedvigf, districtf, streetf)
        q_object = Q()

        if type_uslugf != '0':
            q_object.add(Q(type_uslugi = type_uslugf), Q.AND)
        if type_nedvigf != '0':
            q_object.add(Q(type_nedvig = type_nedvigf), Q.AND)    
        if districtf != '0':
            q_object.add(Q(district = districtf), Q.AND)
        if streetf != '0':
            q_object.add(Q(street = streetf), Q.AND) 
        if prices_start != '' or prices_end != '':
            if prices_start == '':
                prices_start = 0

            if prices_end == '':
                prices_end = 99999999 
            q_object.add(Q(price__range=(prices_start, prices_end)), Q.AND) 

        if komnat1 == 'on' or komnat2 =='on' or komnat3 == 'on' or komnat4 == 'on' or komnat5 == 'on' or Studia == 'on':
            if komnat5 == 'on':
                komnat1 = 1 if komnat1 =='on' else -1
                komnat2 = 2 if komnat2 =='on' else -1
                komnat3 = 3 if komnat3 =='on' else -1
                komnat4 = 4 if komnat4 =='on' else -1
                komnat5 = (5,100) if komnat5 =='on' else (-1,-1)
                Studia = 0 if Studia =='on' else -1
                q_object.add((Q(komnat__in=[komnat1, komnat2, komnat3, komnat4, Studia,]) | Q(komnat__range=(5, 100))), Q.AND)
            else:
                komnat1 = 1 if komnat1 =='on' else -1
                komnat2 = 2 if komnat2 =='on' else -1
                komnat3 = 3 if komnat3 =='on' else -1
                komnat4 = 4 if komnat4 =='on' else -1
                Studia = 0 if Studia =='on' else -1

                q_object.add(Q(komnat__in=[komnat1, komnat2, komnat3, komnat4, Studia,]), Q.AND)

        short = []
        nedvig_list = Nedvigimost.objects.filter(q_object)
        
        for nedvig in nedvig_list:
            title = nedvig.name
            strlen = len(title)
            if strlen > 56:
                n = strlen - 56
                nedvig.name = title[:-n] + '...'
            if strlen < 31:
                short.append(nedvig.pk)
            price = str(nedvig.price)
            strp = ValidPrice(price)   
            nedvig.price = strp
        
        paginator = Paginator(nedvig_list, 3)
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
                   'streets': streets,
                   'short': short}

        return render(request, 'nedvig/catalog.html', context)
        
#Страница недвижимости
class NedvigDetail(View):

    def get(self, request, pk):
        nedvig = Nedvigimost.objects.get(id=pk)
        photo_nedvig = PhotoNedvig.objects.filter(kod_object = pk)
        type_uslugi = TypeUslugi.objects.all()

        count_ph = []
        for i in range(len(photo_nedvig)):
            count_ph.append(i+1)

        price = str(nedvig.price)   

        strp = ValidPrice(price)
        nedvig.price = strp

        nedvig.date_public = nedvig.date_public.strftime('%d.%m.%Y')

        return render(request, 'nedvig/nedvig_page.html', {'nedvig': nedvig, 'photo_nedvig': photo_nedvig, 'count_ph':count_ph, 'type_uslugi':type_uslugi})
    
    def post(self, request, pk):
        tu = TypeUslugi.objects.filter(pk=request.POST.get('Type_Uslugi')).first()
        kod_obj = Nedvigimost.objects.filter(pk=pk).first()

        messages.success(self.request, "Заявка успешно сформирована! Ожидайте звонка в ближайшее время")
        Zayavka = Zayavki.objects.create(FIO = request.POST.get('FIO'), Phone = request.POST.get('Phone'), type_uslugi = tu, kod_object = kod_obj)
        return redirect('catalog')


#Общие функции    
def ValidPrice(price):
    if len(price) == 6:
        strp = price[:3] + ' ' + price[3:]     
    elif len(price) == 7:
        strp = price[:1] + ' ' + price[1:]
        strp = strp[:5] + ' ' + strp[5:]
    elif len(price) == 8: 
        strp = price[:2] + ' ' + price[2:]
        strp = strp[:6] + ' ' + strp[6:]
        strp = strp[:10] + ' ' + strp[10:]
    return strp            