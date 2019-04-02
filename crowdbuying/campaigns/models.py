from django.db import models
import random
import datetime

# Create your models here.

class Campaign(models.Model):
  
  name = models.CharField(max_length=255, unique=True, blank=False)
  duration = models.DurationField(datetime.timedelta(days=30))
  created = models.DateTimeField(auto_now_add=True)
  expiration = models.DateTimeField(blank=True)
  description = models.TextField(max_length=255, blank=True, default="Campaign description...")
  discount = models.IntegerField(default=0)
  
  def random_code():
    return str(random.randint(10000000, 99999999))
  
  slug = models.IntegerField(unique=True, default=random_code)
  
  def __str__(self):
    return self.name
  