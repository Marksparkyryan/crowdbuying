#accounts.models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
from campaigns.models import Campaign


USERNAME_REGEX="^[a-zA-Z0-9.+-]*$"

class MyCustomerManager(BaseUserManager):
	
	def create_user(self, username, email, campaign=None, password=None):
		if not email:
			raise ValueError("Users must have an email address")
		
		user = self.model(
			username=username,
			email = self.normalize_email(email),			
			)
		user.set_password(password)
		user.save(using=self._db)
		return user
		
	def create_superuser(self, username, email, campaign=None, password=None):
		user = self.create_user(
			username, email, campaign, password=password
			)
		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)
		return user
		


class Customer(AbstractBaseUser, PermissionsMixin):
	
	username = models.CharField(
		max_length=300,
		validators = [
			RegexValidator(regex = USERNAME_REGEX,
			message = "Username must be alphanumeric",
			code = "invalid_username"
		)],
		unique=True
		)
	email = models.EmailField(
		max_length=255,
		unique=True,
		verbose_name="email address"
		) 
	campaign = models.ForeignKey(Campaign, verbose_name="Campaign", on_delete=models.CASCADE, null=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	
	objects = MyCustomerManager()
	
	USERNAME_FIELD = "username"
	REQUIRED_FIELDS = ["email"]
	
    