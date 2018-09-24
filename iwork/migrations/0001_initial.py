# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme', models.CharField(max_length=64, verbose_name='\u4f1a\u8bae\u4e3b\u9898')),
                ('content', models.TextField(null=True, verbose_name='\u4f1a\u8bae\u5185\u5bb9', blank=True)),
                ('record_time', models.DateField(auto_now_add=True, verbose_name='\u4f1a\u8bae\u65f6\u95f4')),
                ('operator', models.CharField(max_length=20, verbose_name='\u8bb0\u5f55\u4eba')),
            ],
            options={
                'verbose_name': '\u4f1a\u8bae\u8bb0\u5f55',
                'verbose_name_plural': '\u4f1a\u8bae\u8bb0\u5f55',
            },
        ),
    ]
