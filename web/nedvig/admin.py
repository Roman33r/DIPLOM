from django.contrib import admin
from .models import (Nedvigimost,
                      District,
                      Hozyain,
                      NaselenyiPunkt,
                      PhotoNedvig,
                      Street,
                      Status,
                      TypeNedvig,
                      TypeUchastka,
                      TypeUslugi,
                      Zayavki)

# Register your models here.

class NedvigimostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_nedvig', 'naselenyi_punkt', 'street', 'nomer_doma', 'kvartira', 'date_public', 'publish')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'street', 'naselenyi_punrt')

class PhotoNedvigAdmin(admin.ModelAdmin):
    list_display = ('id', 'path', 'kod_object')
    list_display_links = ('id', 'path', 'kod_object')

class HozyainAdmin(admin.ModelAdmin):
    list_display = ('id', 'FIO', 'phone', 'email')
    list_display_links = ('id', 'FIO')   

class ZayavkiAdmin(admin.ModelAdmin):
    list_display = ('id', 'FIO', 'Phone', 'type_uslugi', 'kod_object', 'status')
    list_display_links = ('id', 'FIO')     

class TypeUslugAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')    

admin.site.register(Nedvigimost, NedvigimostAdmin)
admin.site.register(District)
admin.site.register(Hozyain, HozyainAdmin)
admin.site.register(NaselenyiPunkt)
admin.site.register(PhotoNedvig, PhotoNedvigAdmin)
admin.site.register(Street)
admin.site.register(Status)
admin.site.register(TypeNedvig)
admin.site.register(TypeUchastka)
admin.site.register(TypeUslugi, TypeUslugAdmin)
admin.site.register(Zayavki, ZayavkiAdmin)