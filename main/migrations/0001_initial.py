# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aimag_city',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xd1\x85\xd0\xbe\xd1\x82 \xd0\xb0\xd0\xb9\xd0\xbc\xd0\xb0\xd0\xb3')),
                ('is_country', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'tiim'), (b'0', b'hudal')])),
            ],
            options={
                'verbose_name': 'location \u0430\u0439\u043c\u0430\u0433',
                'verbose_name_plural': 'location \u0430\u0439\u043c\u0430\u0433',
            },
        ),
        migrations.CreateModel(
            name='bag_khoroo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xd0\xb1\xd0\xb0\xd0\xb3 \xd1\x85\xd0\xbe\xd1\x80\xd0\xbe\xd0\xbe\xd0\xbe')),
            ],
            options={
                'verbose_name': 'location \u0431\u0430\u0433',
                'verbose_name_plural': 'location \u0431\u0430\u0433',
            },
        ),
        migrations.CreateModel(
            name='soum_district',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xd1\x81\xd1\x83\xd0\xbc \xd0\xb4\xd2\xaf\xd2\xaf\xd1\x80\xd1\x8d\xd0\xb3')),
                ('aim', models.ForeignKey(to='main.aimag_city', null=True)),
            ],
            options={
                'verbose_name': 'location \u0441\u0443\u043c',
                'verbose_name_plural': 'location \u0441\u0443\u043c',
            },
        ),
        migrations.CreateModel(
            name='Tamgas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'tamga', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='bag_khoroo',
            name='soum',
            field=models.ForeignKey(to='main.soum_district', null=True),
        ),
    ]
