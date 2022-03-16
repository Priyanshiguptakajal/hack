from django.db import models

# Create your models here.
  
class Planets(models.Model):  
    
    name = models.CharField(max_length=50)  
    distance = models.CharField(max_length=100)  
    stars = models.CharField(max_length=100)  
    
    
     
 