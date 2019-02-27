#campaigns.view

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView



class CampaignDetail(DetailView):
	
	template_name = 'campaigns/campaign.html'
	queryset = Campaign.objects.all()
	