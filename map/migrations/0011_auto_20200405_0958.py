# Generated by Django 2.2.7 on 2020-04-05 09:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20200405_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='istoriaviazen',
            name='image_trip',
            field=models.ImageField(default='', upload_to='photos', verbose_name='Timor Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='istoriaviazen',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 5, 9, 58, 19, 108030, tzinfo=utc)),
        ),
    ]
