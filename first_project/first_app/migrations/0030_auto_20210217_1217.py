# Generated by Django 3.1.4 on 2021-02-17 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0029_auto_20210211_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_db',
            name='appoint_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
