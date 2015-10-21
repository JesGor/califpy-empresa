# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alumno', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='calificacion',
            name='empresa',
            field=models.ForeignKey(to='app.Empresa'),
        ),
    ]
