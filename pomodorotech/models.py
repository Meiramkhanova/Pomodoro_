from django.db import models
from django.contrib.auth.models import User


class Pomodoro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(default=25) # default 25 minutes
    break_duration = models.IntegerField(default=5) # default 5 minutes
    is_active = models.BooleanField(default=False)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    pomodoros = models.ManyToManyField(Pomodoro, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pomodoros = models.ManyToManyField(Pomodoro, blank=True)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pomodoro = models.ForeignKey(Pomodoro, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    duration = models.IntegerField()

class BreakLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pomodoro = models.ForeignKey(Pomodoro, on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    duration = models.IntegerField()
