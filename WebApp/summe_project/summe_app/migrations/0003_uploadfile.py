# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summe_app', '0002_remove_file_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('docfile', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
