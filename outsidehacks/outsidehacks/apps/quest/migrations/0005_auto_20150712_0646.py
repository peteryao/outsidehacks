# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quest', '0004_userquest_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbadge',
            old_name='Badge',
            new_name='badge',
        ),
        migrations.AddField(
            model_name='userbadge',
            name='owner',
            field=models.ForeignKey(related_name='user_badges', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
