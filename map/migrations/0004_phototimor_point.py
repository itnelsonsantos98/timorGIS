# Generated by Django 2.2.7 on 2020-02-02 02:41

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_subdistrict'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoTimor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos', verbose_name='Timor Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('description', models.TextField()),
            ],
        ),
    ]
