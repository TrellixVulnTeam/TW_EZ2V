# Generated by Django 2.2.6 on 2019-10-10 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twven', '0002_auto_20191010_1316'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='Tw',
        ),
    ]