# Generated by Django 5.0.6 on 2024-06-26 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvig', '0017_alter_nedvigimost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavki',
            name='kod_object',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET, to='nedvig.nedvigimost', verbose_name='Код объекта'),
        ),
    ]
