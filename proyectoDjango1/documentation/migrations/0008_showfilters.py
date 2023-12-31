# Generated by Django 4.2.6 on 2023-11-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0007_storedprocedurehttp_storedprocedurehttptype'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowFilters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_filter', models.BooleanField(default=True)),
                ('config_filter', models.BooleanField(default=True)),
                ('db_filter', models.BooleanField(default=True)),
                ('docs_filter', models.BooleanField(default=True)),
                ('sp_http_oracle_filter', models.BooleanField(default=True)),
                ('sp_http_sql_filter', models.BooleanField(default=True)),
                ('postman_filter', models.BooleanField(default=True)),
            ],
        ),
    ]
