from django.db import models

# Create your models here.
class Job(models.Model):
    Job_type = [
    ('part_time', 'Part Time'),
    ('full_time', 'Full Time'),
    ]
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    type_job = models.CharField(max_length=40 , choices=Job_type)
    dateline = models.DateField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)