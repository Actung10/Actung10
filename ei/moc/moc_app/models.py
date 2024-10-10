from django.db import models

class Student(models.Model):
    account = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    signature = models.CharField(max_length=200, blank=True)
    memo = models.TextField(blank=True)
    project_count = models.PositiveIntegerField(default=0)
    password = models.CharField(max_length=128, default='')


class Project(models.Model):
    project_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    initiator = models.CharField(max_length=100)
    participants = models.CharField(max_length=200, blank=True)
    supervisor = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    current_members = models.PositiveIntegerField(default=0) 
    total_members = models.PositiveIntegerField(default=0)