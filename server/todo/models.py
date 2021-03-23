from django.db import models
from django.contrib.auth.models import User 

from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Todo(models.Model):
    LOW = 1
    NORMAL = 2
    HIGH = 3
    IMPORTANCE_CHOICES = [
        (LOW, ('Not so Important')),
        (NORMAL, ('Normal Importance')),
        (HIGH, ('Very Important'))
   ]
    UNTOUCHED = 1
    IN_PROGRESS = 2
    DONE = 3
    STATUS_CHOICES = [
        (UNTOUCHED, ('not started')),
        (IN_PROGRESS, ('in progress')),
        (DONE, ('done'))
   ]


    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, default=None)
    importance = models.IntegerField(default=2, choices=IMPORTANCE_CHOICES)
    status = models.IntegerField(default=2, choices=STATUS_CHOICES)