from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(null=True, blank=True)
    user_type = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)


class Project(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class Task(models.Model):
    TASK_STATUS = [('new', 'new'),
                   ('in_progress', 'in_progress'),
                   ('completed', 'completed')
                   ]
    task = models.CharField(max_length=255, null=True, blank=True)
    project = models.ForeignKey(Project, max_length=255, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=255, choices=TASK_STATUS, null=True, blank=True)
