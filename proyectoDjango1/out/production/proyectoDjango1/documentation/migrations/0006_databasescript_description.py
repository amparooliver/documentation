# Generated by Django 3.2.18 on 2023-06-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0005_video_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='databasescript',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción cambio'),
        ),
    ]
