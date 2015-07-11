# SYSTEM DEPENDENCIES
from datetime import datetime

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating "created" and "modified" fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Log(TimeStampedModel):
    user = models.ForeignKey(User)
    record = models.CharField(max_length=1024)
    note = models.CharField(max_length=1024, blank=True)