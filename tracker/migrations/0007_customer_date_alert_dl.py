# Generated by Django 5.0.3 on 2024-03-27 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_alter_customer_options_customer_date_2mil_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_alert_dl',
            field=models.DateField(blank=True, null=True),
        ),
    ]
