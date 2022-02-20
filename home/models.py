#from email.headerregistry import Address
from django.db import models
#from django.forms import PasswordInput

# Create your models here.
class Contact(models.Model):
    Name= models.CharField(max_length=122)
    Email= models.CharField(max_length=122)
    Password= models.CharField(max_length=122)
    Address= models.CharField(max_length=122)

    