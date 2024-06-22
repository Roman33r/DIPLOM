from django.db import models
from datetime import date
# Create your models here.
class TypeUslugi(models.Model):
    name = models.CharField(max_length=512, null=False)
    
    def __str__(self):
        return self.name

class NaselenyiPunkt(models.Model):
    name = models.CharField(max_length=512, null=False)

    def __str__(self):
        return self.name    

class District(models.Model):
    name = models.CharField(max_length=512, null=False)

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=512, null=False)

    def __str__(self):
        return self.name

class TypeNedvig(models.Model):
    name = models.CharField(max_length=512, null=False) 

    def __str__(self):
        return self.name

class TypeUchastka(models.Model):
    name = models.CharField(max_length=512, null=False)

    def __str__(self):
        return self.name

class Hozyain(models.Model):
    FIO = models.CharField(max_length=256, null=False)
    phone = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=512, default=None, null=True)

    def __str__(self):
        return self.FIO
   
class Nedvigimost(models.Model):
    name = models.CharField(max_length=512, null=False)
    naselenyi_punkt = models.ForeignKey(NaselenyiPunkt, on_delete=models.SET)
    district = models.ForeignKey(District, on_delete=models.SET)
    street   = models.ForeignKey(Street, on_delete=models.SET)
    type_nedvig = models.ForeignKey(TypeNedvig, on_delete=models.SET)
    type_uslugi = models.ForeignKey(TypeUslugi, on_delete=models.SET)
    type_uchastka = models.ForeignKey(TypeUchastka, on_delete=models.SET, null=True)
    nomer_doma = models.CharField(max_length=10)
    material = models.CharField(max_length=128)
    main_photo = models.ImageField(upload_to="nedvig_photo")
    obshaya_ploshad = models.FloatField()
    gilaya_ploshad = models.FloatField()
    kuhni_ploshad = models.FloatField()
    uchastka_ploshad = models.FloatField(null=True)
    komnat = models.PositiveIntegerField()
    etag = models.IntegerField()
    etagnost = models.IntegerField()
    price = models.IntegerField(null=False)
    date_public = models.DateField(default=date.today)
    description = models.CharField(max_length=1024)
    hozyain = models.ForeignKey(Hozyain, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PhotoNedvig(models.Model):
    path = models.ImageField(upload_to="nedvig_photo", null=False)
    kod_object = models.ForeignKey(Nedvigimost, on_delete=models.SET, null=False)

    def __str__(self):
        return str(self.path) 

class Status(models.Model):
    name = models.CharField(max_length=56)

    def __str__(self):
        return self.name

class Zayavki(models.Model):
    FIO = models.CharField(max_length=256)
    Phone = models.CharField(max_length=20)
    type_uslugi  = models.ForeignKey(TypeUslugi, on_delete=models.SET)
    status = models.ForeignKey(Status, on_delete=models.SET, default=1)

    def __str__(self):
        return self.FIO