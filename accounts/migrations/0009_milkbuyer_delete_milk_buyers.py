# Generated by Django 5.1.3 on 2024-11-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_milk_buyers_delete_purchasers'),
    ]

    operations = [
        migrations.CreateModel(
            name='MilkBuyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('companyname', models.CharField(max_length=100)),
                ('prn', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='milk_Buyers',
        ),
    ]
