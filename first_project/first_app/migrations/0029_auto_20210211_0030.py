# Generated by Django 3.1.4 on 2021-02-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0028_appointment_db'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_db',
            name='appoint_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
