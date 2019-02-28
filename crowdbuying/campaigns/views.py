#campaigns.view

# Create your views here.
from django.views.generic import DetailView
from . import models



class CampaignDetail(DetailView):
  
  template_name = 'campaigns/campaign.html'
  model = models.Campaign
     
      