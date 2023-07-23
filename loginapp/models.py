from django.db import models

# Create your models here.

class signup(models.Model):
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    secondname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    pass1= models.CharField(max_length=200)
    pass2 = models.CharField(max_length=200)
   
   
