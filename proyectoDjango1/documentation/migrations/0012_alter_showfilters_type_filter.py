# Generated by Django 4.2.6 on 2023-11-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0011_showfilters_name_filter_showfilters_type_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showfilters',
            name='type_filter',
            field=models.BooleanField(default=False, verbose_name='Mostrar Filtro'),
        ),
    ]