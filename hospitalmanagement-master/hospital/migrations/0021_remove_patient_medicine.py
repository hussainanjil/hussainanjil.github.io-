# Generated by Django 3.0.5 on 2021-05-31 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20210531_2315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='medicine',
        ),
    ]
