# Generated by Django 5.0.4 on 2024-04-13 16:10

import django_jalali.db.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_transfer_options_alter_transfer_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]
