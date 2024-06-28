from django.db import models
from datetime import date
# Create your models here.
class TypeUslugi(models.Model):
    name = models.CharField("Наименование", max_length=512, null=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'

class NaselenyiPunkt(models.Model):
    name = models.CharField("Наименование", max_length=512, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенный пункты'    

class District(models.Model):
    name = models.CharField("Наименование", max_length=512, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

class Street(models.Model):
    name = models.CharField("Наименование", max_length=512, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'

class TypeNedvig(models.Model):
    name = models.CharField("Наименование", max_length=512, null=False) 

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'

class TypeUchastka(models.Model):
    name = models.CharField("Наименование", max_length=512, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип участка'
        verbose_name_plural = 'Типы участков'

class Hozyain(models.Model):
    FIO = models.CharField("ФИО", max_length=256)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("E-mail", max_length=512, default=None, blank=True)

    def __str__(self):
        return self.FIO
    
    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
   
class Nedvigimost(models.Model):
    name = models.CharField("Заголовок", max_length=256)
    naselenyi_punkt = models.ForeignKey(NaselenyiPunkt, verbose_name="Населенный пункт", on_delete=models.SET)
    district = models.ForeignKey(District, verbose_name="Район", on_delete=models.SET)
    street   = models.ForeignKey(Street, verbose_name="Улица", on_delete=models.SET)
    type_nedvig = models.ForeignKey(TypeNedvig, verbose_name="Тип недвижимости", on_delete=models.SET)
    type_uslugi = models.ForeignKey(TypeUslugi, verbose_name="Тип услуги", on_delete=models.SET)
    type_uchastka = models.ForeignKey(TypeUchastka, verbose_name="Тип участка", on_delete=models.SET, blank=True, default=None, null=True)
    nomer_doma = models.CharField("Номер дома", max_length=10)
    kvartira = models.IntegerField("Квартира", max_length=5, blank=True, default=None, null=True)
    material = models.CharField("Материал", max_length=128)
    main_photo = models.ImageField("Основное фото", upload_to="nedvig_photo")
    obshaya_ploshad = models.FloatField("Общая площадь")
    gilaya_ploshad = models.FloatField("Жилая площадь")
    kuhni_ploshad = models.FloatField("Площадь кухни")
    uchastka_ploshad = models.FloatField("Площадь участка", blank=True, default=None, null=True)
    komnat = models.PositiveIntegerField("Комнатность")
    etag = models.IntegerField("Этаж")
    etagnost = models.IntegerField("Этажность")
    price = models.IntegerField("Цена", blank=False)
    date_public = models.DateField("Дата публикации", default=date.today)
    description = models.TextField("Описание")
    hozyain = models.ForeignKey(Hozyain, verbose_name="Хозяин", on_delete=models.CASCADE)
    publish = models.BooleanField("Публиковать", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Недвижимость'

class PhotoNedvig(models.Model):
    path = models.ImageField("Путь к файлу", upload_to="nedvig_photo", blank=False)
    kod_object = models.ForeignKey(Nedvigimost, verbose_name="Код объекта", on_delete=models.SET, blank=False)

    def __str__(self):
        return str(self.path) 
    
    class Meta:
        verbose_name = 'Фото недвижимости'
        verbose_name_plural = 'Фото недвижимости'

class Status(models.Model):
    name = models.CharField("Наименование", max_length=56)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'

class Zayavki(models.Model):
    FIO = models.CharField("ФИО", max_length=256)
    Phone = models.CharField("Телефон", max_length=20)
    type_uslugi  = models.ForeignKey(TypeUslugi, verbose_name="Тип услуги", on_delete=models.SET)
    status = models.ForeignKey(Status, verbose_name="Статус заявки", on_delete=models.SET, default=1)
    kod_object = models.ForeignKey(Nedvigimost, verbose_name="Код объекта", on_delete=models.SET, blank=True, default=None, null=True)

    def __str__(self):
        return self.FIO
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'