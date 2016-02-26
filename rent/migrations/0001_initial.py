# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_start', models.DateTimeField()),
                ('contract_expected_end', models.DateTimeField()),
                ('contract_real_end', models.DateTimeField()),
                ('miles_in', models.IntegerField()),
                ('miles_out', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('vat_code', models.CharField(max_length=100)),
                ('ssn', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('driving_licence', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField()),
                ('invoice_date', models.DateTimeField()),
                ('invoice_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('is_payed', models.BooleanField(default=False)),
                ('date_payed', models.DateTimeField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('plate', models.CharField(max_length=12)),
                ('miles', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Customer'),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.Vehicle'),
        ),
    ]
