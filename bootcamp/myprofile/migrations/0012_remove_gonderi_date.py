# Generated by Django 4.0.4 on 2022-05-20 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0011_gonderi_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gonderi',
            name='date',
        ),
    ]