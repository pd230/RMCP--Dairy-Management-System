# Generated by Django 5.1.3 on 2024-11-26 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_milkbuyer_delete_milk_buyers'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.milkbuyer')),
            ],
        ),
    ]