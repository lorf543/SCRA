# Generated by Django 5.0.4 on 2024-04-13 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scra_inbox', '0005_remove_inbox_sent_by'),
        ('tracker', '0009_alter_address_options_alter_account_added_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_inbox', to='tracker.account'),
        ),
    ]
