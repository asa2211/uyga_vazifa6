from django.db import models
from datetime import datetime


class SubjectModel(models.Model):
    subject_name = models.CharField(default='', max_length=200)
    added_at = models.DateTimeField(datetime.now)
