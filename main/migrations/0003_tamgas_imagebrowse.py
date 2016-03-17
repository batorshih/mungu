# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160317_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='tamgas',
            name='imagebrowse',
            field=filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'Image', blank=True),
        ),
    ]
