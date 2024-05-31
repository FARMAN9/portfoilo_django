from django.urls import path
from  main import views



urlpatterns=[
   
    
   

path('', views.index.as_view(), name='index'),
    path('datasend/',views.Datasend,name='datasend'),
     path('datanotsend/',views.Datasend,name='datanotsend'),
     path('Project/<int:id>/',views.ProjectView.as_view(),name='project')

]