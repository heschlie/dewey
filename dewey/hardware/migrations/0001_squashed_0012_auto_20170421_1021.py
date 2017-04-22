# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-21 18:01
from __future__ import unicode_literals

import dewey.hardware
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    replaces = [('hardware', '0001_initial'), ('hardware', '0002_auto_20150924_1538'), ('hardware', '0003_server_rack_units'), ('hardware', '0004_auto_20150929_1604'), ('hardware', '0005_auto_20150930_1053'), ('hardware', '0006_auto_20150930_1116'), ('hardware', '0007_auto_20150930_1334'), ('hardware', '0008_auto_20151006_1141'), ('hardware', '0009_auto_20151006_1647'), ('hardware', '0010_auto_20160511_1438'), ('hardware', '0011_auto_20170420_1529'), ('hardware', '0012_auto_20170421_1021')]

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('rack_units', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Datacenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('vendor', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('noc_phone', models.CharField(blank=True, max_length=24)),
                ('noc_email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ephor_id', models.PositiveIntegerField(unique=True)),
                ('asset_tag', models.CharField(max_length=128)),
                ('manufacturer', models.CharField(blank=True, max_length=128)),
                ('model', models.CharField(blank=True, max_length=128)),
                ('serial', models.CharField(blank=True, max_length=256)),
                ('rack_units', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='cabinet',
            name='datacenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Datacenter'),
        ),
        migrations.CreateModel(
            name='CabinetAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField(blank=True, null=True)),
                ('orientation', enumfields.fields.EnumIntegerField(blank=True, enum=dewey.hardware.RackOrientation, null=True)),
                ('equipment_id', models.PositiveIntegerField()),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hardware.Cabinet')),
                ('equipment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('depth', enumfields.fields.EnumIntegerField(blank=True, enum=dewey.hardware.RackDepth, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.PositiveIntegerField()),
                ('port', models.PositiveIntegerField()),
                ('connected_device_id', models.PositiveIntegerField()),
                ('connected_device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_device', to='contenttypes.ContentType')),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='port_assignment', to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='PowerDistributionUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ephor_id', models.PositiveIntegerField(unique=True)),
                ('asset_tag', models.CharField(max_length=128)),
                ('manufacturer', models.CharField(blank=True, max_length=128)),
                ('model', models.CharField(blank=True, max_length=128)),
                ('serial', models.CharField(blank=True, max_length=256)),
                ('rack_units', models.IntegerField(blank=True, null=True)),
                ('volts', models.PositiveIntegerField()),
                ('amps', models.PositiveIntegerField()),
                ('ports', models.PositiveIntegerField()),
                ('description', models.CharField(blank=True, max_length=256)),
                ('name', models.SlugField(default='pdu')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ephor_id', models.PositiveIntegerField(unique=True)),
                ('asset_tag', models.CharField(max_length=128)),
                ('manufacturer', models.CharField(blank=True, max_length=128)),
                ('model', models.CharField(blank=True, max_length=128)),
                ('serial', models.CharField(blank=True, max_length=256)),
                ('rack_units', models.IntegerField(blank=True, null=True)),
                ('name', models.SlugField()),
                ('description', models.CharField(blank=True, max_length=256)),
                ('ports', models.PositiveIntegerField()),
                ('speed', enumfields.fields.EnumIntegerField(enum=dewey.hardware.SwitchSpeed)),
                ('interconnect', enumfields.fields.EnumIntegerField(enum=dewey.hardware.SwitchInterconnect)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cabinet',
            name='posts',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='rack_units',
            field=models.PositiveIntegerField(),
        ),
    ]