# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='owner',
            field=models.ForeignKey(related_name='badges', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
