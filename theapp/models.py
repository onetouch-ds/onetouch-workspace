from django.db import models

# Create your models here.

class NoticeTable(models.Model):
    num = models.IntegerField()
    title = models.TextField()
    author = models.TextField()
    click = models.IntegerField()
    date = models.DateTimeField()
