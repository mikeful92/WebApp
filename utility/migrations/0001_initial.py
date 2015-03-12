# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricConsumption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_address', models.CharField(max_length=200)),
                ('service_city', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('kwh_consumption', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
