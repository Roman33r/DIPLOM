# Generated by Django 5.0.6 on 2024-06-26 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvig', '0013_alter_nedvigimost_uchastka_ploshad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nedvigimost',
            name='kvartira',
            field=models.IntegerField(blank=True, default=None, max_length=5, null=True, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='nedvigimost',
            name='type_uchastka',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET, to='nedvig.typeuchastka', verbose_name='Тип участка'),
        ),
        migrations.AlterField(
            model_name='nedvigimost',
            name='uchastka_ploshad',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Площадь участка'),
        ),
    ]
