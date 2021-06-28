from django.db import models

class DataReturn(models.Model):
    comments_qty = models.IntegerField
    comments_author = models.CharField(max_length=400)
    comments_date = models.DateField


