from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Landing(TemplateView):
  template_name="landing/landing.html"
  