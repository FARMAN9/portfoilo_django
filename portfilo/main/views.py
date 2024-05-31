from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from .forms import *
from django.contrib import messages
from .models import*
from django.urls import reverse

# Create your views here.
from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

class index(TemplateView):
    main_data = 'jjj'#Smainx.objects.get(id=1)
    skills=skills.objects.all()
    portfolios=Projects.objects.all()
    eduction=Eduction.objects.all()
    Professionals=Professional_Experience.objects.all()
    sumary= 1#summery.objects.get(id=1)
    template_name='index.html'
    def  get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['Name'] ='Syed Farman Ali'
        context['Phone'] ='+91 6005943382'
        context['Email'] ='saeedfarman9@gmail.com'
        context['address'] ='Pulwama J&K India'
        context['form'] = ContactForm()
        context['main']=self.main_data
        context['skill_list']=self.skills.all()
        context['age']=calculateAge(date(1998, 9, 15))
        context['portfolio_list']=self.portfolios.all()
        context['eductions']=self.eduction.all()
        context['Professionals']=self.Professionals.all()
        context['sumary']=self.sumary
      
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
           
   


class ProjectView(TemplateView):
    template_name = 'portfolio-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = kwargs.get('id')  # Retrieve the id parameter from URL
        data = Projects.objects.get(id=project_id)
        context['Name'] = 'Syed Farman ali'
        context['Phone'] = '+91 6005943382'
        context['Email'] = 'saeedfarman9@gmail.com'
        context['address'] = 'Pulwama J&K India'
        context['data'] = data
        return context
















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







