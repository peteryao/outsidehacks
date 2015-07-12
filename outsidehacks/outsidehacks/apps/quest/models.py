# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date
import requests

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

class Quest(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField()
    points_awarded = models.IntegerField()