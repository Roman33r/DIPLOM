# Generated by Django 5.0.6 on 2024-06-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvig', '0014_alter_nedvigimost_kvartira_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nedvigimost',
            name='description',
            field=models.CharField(max_length=4096, verbose_name='Описание'),
        ),
    ]
