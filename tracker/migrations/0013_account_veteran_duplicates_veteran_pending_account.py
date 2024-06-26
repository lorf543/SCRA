# Generated by Django 5.0.4 on 2024-05-19 01:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_alter_duplicates_created_alter_duplicates_updated'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='veteran',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='duplicates',
            name='veteran',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='Pending_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(blank=True, max_length=50, null=True)),
                ('pending_note', models.TextField(blank=True, null=True)),
                ('resolve_note', models.TextField(blank=True, null=True)),
                ('resolve_date', models.DateField(auto_now_add=True, null=True)),
                ('resolve', models.BooleanField(blank=True, default=False, null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('updated', models.DateField(blank=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending_add', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending_customer', to='tracker.account')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending_update', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
