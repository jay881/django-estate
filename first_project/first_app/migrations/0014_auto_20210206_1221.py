# Generated by Django 3.1.4 on 2021-02-06 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_auto_20210206_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flats_info',
            name='pic',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]