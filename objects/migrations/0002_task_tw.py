# Generated by Django 2.2.6 on 2019-10-10 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('taskNumber', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('currentTask', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now=True)),
                ('date1_start', models.DateField(default=None)),
                ('date1_end', models.DateField(default=None)),
                ('date2_start', models.DateField(default=None)),
                ('date2_end', models.DateField(default=None)),
                ('date3_start', models.DateField(default=None)),
                ('date3_end', models.DateField(default=None)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Object')),
            ],
        ),
    ]
