# Generated by Django 3.1.4 on 2021-02-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0024_auto_20210207_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='flats_info',
            name='property_image_one',
            field=models.ImageField(default='', upload_to='media/flats_img'),
        ),
    ]