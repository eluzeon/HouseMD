# Generated by Django 2.0.3 on 2018-04-06 18:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0011_auto_20180406_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysisconstants',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='disease',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='symptom',
            name='counter',
        ),
    ]
