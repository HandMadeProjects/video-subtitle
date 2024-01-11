from django.db import models
from django.utils import timezone


# Create your models here.

class Videos(models.Model):
    v_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="")
    v_path = models.CharField(max_length=200, default="")
    sub_path = models.CharField(max_length=200, default="")
    upload_date = models.DateField(default=timezone.now)

    # category = models.CharField(max_length=50, default="")
    
    def __str__(self):
        return self.title