# Generated by Django 5.0.4 on 2024-06-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0022_alter_account_approved_date_alter_account_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='qualify',
            field=models.CharField(blank=True, choices=[('approved', 'approved'), ('not approved', 'not approved')], max_length=50, null=True),
        ),
    ]
