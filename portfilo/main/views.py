from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from django.contrib import messages
from .models import*
from django.urls import reverse

# Create your views here.

class index(TemplateView):
    template_name='index.html'
    def  get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['Name'] ='Syed Farman ali'
        context['Phone'] ='+91 6005943382'
        context['Email'] ='saeedfarman9@gmail.com'
        context['address'] ='Pulwama J&K India'
        context['form'] = ContactForm()
        return context
    def post(self, request, *args, **kwargs):
        # Handle form submission
        form = ContactForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the data
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            # Redirect to a success URL or reload the page
            return redirect(reverse('datasend')) 
        else:
            # If the form is invalid, render the page with the form and errors
            messages.error(request, "There was an error submitting the form.")
            return redirect(reverse('datanotsend')) 
           
   

from django.http import HttpResponse

def Datasend(request):
    # Check request.method if needed to handle different HTTP methods
    # For now, let's assume we just want to return a simple text response.
    return HttpResponse("Message has been sent successfully.")

def DataNotsend(request):
    # Check request.method if needed to handle different HTTP methods
    # For now, let's assume we just want to return a simple text response.
    return HttpResponse("Invalid")





   
          


        
    



class projects():



    def  get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['Name'] ='Syed Farman ali'
        context['Phone'] ='+91 6005943382'
        context['Email'] ='saeedfarman9@gmail.com'
        context['address'] ='Pulwama J&K India'
        return context







