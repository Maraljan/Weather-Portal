# Generated by Django 3.2.7 on 2021-10-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_cityweatherinfo_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityweatherinfo',
            name='icon',
            field=models.CharField(max_length=30),
        ),
    ]
