# Generated by Django 3.1.4 on 2021-02-07 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0020_auto_20210207_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='bungalows_info',
            name='seller_db',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='first_app.seller_info'),
        ),
    ]
