#accounts.admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomerCreationForm

from accounts.models import Customer, Campaign

class UserAdmin(BaseUserAdmin):
	add_form = CustomerCreationForm
	
	
	list_display = ("username", "email", "campaign", "is_superuser")
	list_filter = ("campaign",)
	
	fieldsets = (
		(None, {"fields":("username", "email", "campaign", "password",)}),
		("Permissions", {"fields":("is_superuser",)})
		)
	search_fields = ("username", "email", "campaign",)
	ordering = ("username", "email",)
	filter_horizontal = ()
  
  
admin.site.register(Customer, UserAdmin)

