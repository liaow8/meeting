# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0002_auto_20180922_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workrecord',
            options={'ordering': ['-id'], 'verbose_name': '\u4f1a\u8bae\u8bb0\u5f55', 'verbose_name_plural': '\u4f1a\u8bae\u8bb0\u5f55'},
        ),
    ]
