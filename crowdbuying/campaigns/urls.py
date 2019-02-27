from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
  path("<int:slug>", CampaignDetail.as_view()),
	]