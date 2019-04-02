#campaigns.view

# Create your views here.
from django.views.generic import DetailView
from . import models
import datetime 
from accounts.models import Customer



class CampaignDetail(DetailView):
  
  template_name = 'campaigns/campaign.html'
  model = models.Campaign
  
  def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.expiration = obj.created + datetime.timedelta(days=30)
        obj.save()
        return obj
  
  def get_context_data(self, **kwargs):
        # xxx will be available in the template as the related objects
        context = super(CampaignDetail, self).get_context_data(**kwargs)
        context['members'] = Customer.objects.filter(campaign=self.get_object())
        return context
  
  
    
  
     
      