from django.db import models

# Create your models here.

class Campaign(models.Model):
	
	name = models.CharField(max_length=255, unique=True, default="Campaign name...")
	description = models.TextField(blank=True, default="Campaign description...")
	members = models.ManyToManyField('accounts.Customer', related_name="membership")	
	
	def random_code():
		return str(random.randint(10000000, 99999999))

	
	slug = models.IntegerField(unique=True, default=random_code)
	
	def __str__(self):
		return self.name
  
  