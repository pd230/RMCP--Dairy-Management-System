# Generated by Django 5.1.3 on 2024-11-25 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_milk_pricing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milk_pricing',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, unique=True),
        ),
    ]
