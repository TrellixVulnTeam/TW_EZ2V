# Generated by Django 2.2.6 on 2019-10-11 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_auto_20191010_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tw',
            name='date',
            field=models.CharField(default=datetime.datetime(2019, 10, 11, 6, 21, 1, 282620), max_length=100),
        ),
    ]