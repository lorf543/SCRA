# Generated by Django 5.0.4 on 2024-05-05 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_alter_address_options_alter_account_added_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Fees',
            field=models.CharField(blank=True, default='N/A', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='Interest_Rate',
            field=models.CharField(blank=True, default='N/A', max_length=50, null=True),
        ),
    ]
