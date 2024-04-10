# Generated by Django 5.0.4 on 2024-04-08 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('En', 'Entry'), ('Ex', 'Exit')], max_length=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('from_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_from', to='employee.employee')),
                ('to_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transfers_to', to='employee.employee')),
            ],
        ),
        migrations.CreateModel(
            name='TransferItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='home.transfer')),
            ],
        ),
    ]