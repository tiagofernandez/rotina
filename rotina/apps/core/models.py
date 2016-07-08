import time

from croniter import croniter
from datetime import datetime
from hashids import Hashids

from django.db import models

from rotina.libs.database import get_or_none

class Routine(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=2, choices=(
        ('EV', 'Event'),
        ('GL', 'Grocery List'),
        ('TA', 'Task'),
    ))
    cron = models.CharField(max_length=100) # http://en.wikipedia.org/wiki/Cron

    class Meta:
        db_table = 'routine'

    HASHIDS = Hashids(salt='R0T1N4', alphabet='ABCDEFGHJKLMNPQRSTUVWXYZ23456789', min_length=6)

    @classmethod
    def generate_code(cls):
        return cls.HASHIDS.encrypt(round(time.time()))[:10]

    def next_occurrence(self, base=datetime.now()):
        occurences = croniter(self.cron, base)
        return occurences.get_next(datetime)

    @staticmethod
    def get_by_code(code):
        return get_or_none(Routine, code=code)

class Instance(models.Model):
    routine = models.ForeignKey(Routine)
    occurrence = models.DateTimeField()

    class Meta:
        db_table = 'instance'

class Comment(models.Model):
    instance = models.ForeignKey(Instance)
    timestamp = models.DateTimeField()
    nickname = models.CharField(max_length=20)
    text = models.CharField(max_length=140)

    class Meta:
        db_table = 'comment'

class Event(models.Model):
    instance = models.ForeignKey(Instance)
    nickname = models.CharField(max_length=20)
    rsvp = models.CharField(max_length=1, choices=(
        ('Y', 'Yes'),
        ('N', 'No'),
        ('M', 'Maybe'),
    ))

    class Meta:
        db_table = 'event'

class GroceryList(models.Model):
    instance = models.ForeignKey(Instance)
    items = models.TextField(default='{}')

    class Meta:
        db_table = 'grocery_list'

class Task(models.Model):
    instance = models.ForeignKey(Instance)
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'task'
