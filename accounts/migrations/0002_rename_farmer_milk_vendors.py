# Generated by Django 5.1.3 on 2024-11-21 10:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Farmer',
            new_name='milk_vendors',
        ),
    ]
