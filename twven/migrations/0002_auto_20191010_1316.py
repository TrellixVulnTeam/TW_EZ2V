# Generated by Django 2.2.6 on 2019-10-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twven', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tw',
            name='objectId',
        ),
        migrations.AlterField(
            model_name='tw',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
