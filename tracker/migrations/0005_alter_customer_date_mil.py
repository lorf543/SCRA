# Generated by Django 5.0.3 on 2024-03-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_alter_customer_options_customer_date_mil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_mil',
            field=models.DateField(blank=True, null=True),
        ),
    ]
