from django.db import models

# Create your models here.


class DailyNote(models.Model):

    title = models.CharField(max_length=100)
