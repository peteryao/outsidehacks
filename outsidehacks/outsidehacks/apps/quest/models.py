# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# PROJECT DEPENDENCIES

# APP DEPENDENCIES
from outsidehacks.apps.core.models import *

# Create your models here.
class Zone(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField()
    time_start = models.DateTimeField(blank=True, null=True)
    time_end = models.DateTimeField(blank=True, null=True)

    owner = models.ForeignKey('auth.User', related_name='zones')

    def __unicode__(self):
        return self.name

class Badge(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField()

    owner = models.ForeignKey('auth.User', related_name='badges')

class Cateogry(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField()

    owner = models.ForeignKey('auth.User', related_name='quests_category')

class Quest(TimeStampedModel):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Cateogry)
    description = models.CharField(max_length=1000)
    image = models.ImageField()
    points_awarded = models.IntegerField()
    zone = models.ForeignKey(Zone)

    owner = models.ForeignKey('auth.User', related_name='quests')

class UserQuest(TimeStampedModel):
    user = models.ForeignKey(User)
    quest = models.ForeignKey(Quest)
    completed = models.BooleanField(default=False)

    owner = models.ForeignKey('auth.User', related_name='user_quests')

class UserBadge(TimeStampedModel):
    user = models.ForeignKey(User)
    badge = models.ForeignKey(Badge)

    owner = models.ForeignKey('auth.User', related_name='user_badges')