# Generated by Django 5.1.3 on 2024-11-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_milk_vendors_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='milk_pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.CharField(choices=[('Premium', 'Premium'), ('Standard', 'Standard'), ('Organic', 'Organic'), ('Low-fat', 'Low-fat'), ('Full Cream', 'Full Cream')], max_length=20)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('price_per_liter', models.DecimalField(decimal_places=2, max_digits=6)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Milk Pricing',
                'verbose_name_plural': 'Milk Pricing',
            },
        ),
    ]