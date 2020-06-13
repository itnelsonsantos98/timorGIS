# Generated by Django 2.2.10 on 2020-06-13 00:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_delete_point'),
    ]

    operations = [
        migrations.RenameField(
            model_name='istoriaviazen',
            old_name='upload_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='istoriaviazen',
            old_name='date',
            new_name='duration_of_trip',
        ),
        migrations.AddField(
            model_name='istoriaviazen',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='phototimor',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='phototimor',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='phototimor',
            name='istoriaviazen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='map.IstoriaViazen'),
        ),
    ]
