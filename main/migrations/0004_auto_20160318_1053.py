# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tamgas_imagebrowse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tamgas',
            options={'verbose_name': '\u0442\u0430\u043c\u0433\u0430-'},
        ),
        migrations.RemoveField(
            model_name='tamgas',
            name='imagebrowse',
        ),
    ]
