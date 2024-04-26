from django.shortcuts import render
from django.views.generic import View,TemplateView


# Create your views here.

class index(TemplateView):
    template_name='index.html'
    def  get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['Name'] ='Syed Farman ali'
        context['Phone'] ='+91 6005943382'
        context['Email'] ='saeedfarman9@gmail.com'
        context['address'] ='Pulwama J&K India'
        return context

