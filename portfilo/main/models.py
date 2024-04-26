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
