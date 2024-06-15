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
admin.site.register(Nedvigimost)
admin.site.register(District)
admin.site.register(Hozyain)
admin.site.register(NaselenyiPunkt)
admin.site.register(PhotoNedvig)
admin.site.register(Street)
admin.site.register(Status)
admin.site.register(TypeNedvig)
admin.site.register(TypeUchastka)
admin.site.register(TypeUslugi)
admin.site.register(Zayavki)