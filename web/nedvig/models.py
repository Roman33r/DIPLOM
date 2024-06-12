from django.db import models

# Create your models here.
class TypeUslugi(models.Model):
    name = models.CharField(max_length=512)

class NaselenyiPunkt(models.Model):
    name = models.CharField(max_length=512)    

class District(models.Model):
    name = models.CharField(max_length=512)

class Street(models.Model):
    name = models.CharField(max_length=512)

class TypeNedvig(models.Model):
    name = models.CharField(max_length=512) 

class TypeUchastka(models.Model):
    name = models.CharField(max_length=512)

class Hozyain(models.Model):
    FIO = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=512, default=None)
   
class Nedvigimost(models.Model):
    name = models.CharField(max_length=512)
    naselenyi_punkt = models.ForeignKey(NaselenyiPunkt, on_delete=models.SET)
    district = models.ForeignKey(District, on_delete=models.SET)
    street   = models.ForeignKey(Street, on_delete=models.SET)
    type_nedvig = models.ForeignKey(TypeNedvig, on_delete=models.SET)
    type_uchastka = models.ForeignKey(TypeUchastka, on_delete=models.SET, null=True)
    nomer_doma = models.CharField(max_length=10)
    material = models.CharField(max_length=128)
    main_photo = models.CharField(max_length=512)
    obshaya_ploshad = models.FloatField()
    gilaya_ploshad = models.FloatField()
    kuhni_ploshad = models.FloatField()
    uchastka_ploshad = models.FloatField(null=True)
    komnat = models.IntegerField()
    etag = models.IntegerField()
    etagnost = models.IntegerField()
    price = models.IntegerField()
    date_public = models.DateField()
    description = models.CharField(max_length=1024)
    hozyain = models.ForeignKey(Hozyain, on_delete=models.CASCADE)

class PhotoNedvig(models.Model):
    path = models.CharField(max_length=512)
    kod_object = models.ForeignKey(Nedvigimost, on_delete=models.SET) 

class Status(models.Model):
    name = models.CharField(max_length=56)

class Zayavki(models.Model):
    FIO = models.CharField(max_length=256)
    Phone = models.CharField(max_length=20)
    type_uslugi  = models.ForeignKey(TypeUslugi, on_delete=models.SET)
    status = models.ForeignKey(Status, on_delete=models.SET)