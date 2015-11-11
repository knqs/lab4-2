# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.AutoField(serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ISBN', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=50)),
                ('Publisher', models.CharField(max_length=50)),
                ('PublishDate', models.DateField()),
                ('Price', models.FloatField()),
                ('AuthorID', models.ForeignKey(to='mylib.Author', null=True)),
            ],
        ),
    ]
