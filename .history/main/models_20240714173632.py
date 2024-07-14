from django.db import models


# Create your models here.


class Contact(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    name =models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=255)
    message=models.TextField(max_length=255)
    def __str__(self):
        return self.name+str(self.date)
    


class Projects(models.Model):
     name =models.CharField(max_length=50)
     project_url=models.URLField(null=True)
     client=models.CharField(max_length=50,null=True, blank=True)
     description=models.TextField(max_length=255,null=True, blank=True)
     date = models.DateTimeField(auto_now_add=True)
     image1 = models.ImageField(upload_to='images/')
     image2 = models.ImageField(upload_to='images/',null=True,blank=True)
     image3 = models.ImageField(upload_to='images/',null=True,blank=True)
     def __str__(self):
        return self.name+str(self.date)
class Eduction (models.Model):
     name =models.CharField(max_length=100)
     frm = models.CharField(max_length=100)
     to = models.CharField(max_length=100,default='Present')
     address=models.CharField(max_length=100)
     about=models.CharField(max_length=255)
     def __str__(self):
        return self.name
class Professional_Experience(models.Model):
      name =models.CharField(max_length=100)
      frm = models.CharField(max_length=100)
      to = models.CharField(max_length=100,default='present')
      address=models.CharField(max_length=100)
      p1= models.CharField(max_length=255)
      p2= models.CharField(max_length=255) 
      p3= models.CharField(max_length=255) 
      p4= models.CharField(max_length=255)     
      def __str__(self):
        return self.name
class skills (models.Model):
    name=models.CharField(max_length=100)
    val=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class summery (models.Model):
     summery =models.CharField(max_length=255)
     address=models.CharField(max_length=100)
     email=models.CharField(max_length=255,null= True)
     phone=models.CharField(max_length=12,null= True)
     name=models.CharField(max_length=100,null= True,default='Syed Farman Ali')
     
     
     
        

class mainx(models.Model):
    about= models.CharField(max_length=100,default=' ',null= True) 
    cantact= models.CharField(max_length=100,default=' ',null= True)
    portfilo= models.CharField(max_length=100,default=' ',null= True) 
    resume= models.CharField(max_length=100,default=' ',null= True)
    Skills=models.CharField(max_length=100,default=' ',null= True)
    certificates=models.CharField(max_length=100,default=' ',null= True)
    profile=models.ImageField(upload_to='images/')
    
    iam1=models.CharField(max_length=100,default='Developer',null= True) 
    iam2=models.CharField(max_length=100,default='Developer',null= True) 
    iam3=models.CharField(max_length=100,default='Developer',null= True) 
    iam4=models.CharField(max_length=100,default='Developer',null= True)
    
    def __str__(self):
        return self.about
    
class  certificates(models.Model):
    name=models.CharField(max_length=100,null= True)  
    link=models.URLField(null=True)
    image1 = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name


