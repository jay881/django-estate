# Generated by Django 3.1.4 on 2021-02-06 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0016_flats_info_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flats_info',
            name='seller',
        ),
    ]
