# Generated by Django 2.1.2 on 2018-11-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0012_auto_20181111_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imgMascota',
            field=models.ImageField(upload_to='images/mascotas/'),
        ),
    ]