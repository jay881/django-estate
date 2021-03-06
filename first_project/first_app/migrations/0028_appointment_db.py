# Generated by Django 3.1.4 on 2021-02-10 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0027_auto_20210210_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoint_date', models.CharField(default='', max_length=50)),
                ('app_st', models.BooleanField(default=False)),
                ('buyer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='first_app.buyer')),
                ('seller', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='first_app.seller_info')),
            ],
        ),
    ]
